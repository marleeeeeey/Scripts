import sys
from typing import Dict, List, Any, Tuple, Union
from googletrans import Translator
import genanki
from google_speech import Speech
import os
import random
from google_images_download import google_images_download
from PIL import Image


class Bucket:
    def __init__(self):
        self.word = ""
        self.word_translation = ""
        self.word_sound_path = ""
        self.meaning_sound_path = ""
        self.meaning = ""
        self.meaning_translation = ""
        self.example = ""
        self.example_translation = ""
        self.path_to_picture = ""

    def process(self, output_directory):
        self.generate_translations()
        self.generate_speech(output_directory)
        try:
            self.generate_pictures(output_directory)
        except AttributeError:
            self.path_to_picture = ""
            print("Can't generate image", self.word)

    def generate_translations(self):
        self.example_translation = Helper.translate(self.example)
        self.meaning_translation = Helper.translate(self.meaning)
        self.word_translation = Helper.translate(self.word)

    def generate_speech(self, output_directory):
        self.word_sound_path = Helper.save_speech_to(self.word, output_directory, "en")
        self.meaning_sound_path = Helper.save_speech_to(self.meaning, output_directory, "en")

    def generate_pictures(self, output_directory):
        count_of_pictures = 1  # TODO
        basewidth = 400
        pictures = Helper.load_pictures_to_download_subfolder(self.word, output_directory, count_of_pictures)
        if (len(pictures) != 0):
            self.path_to_picture = pictures[0]
            Helper.resize_image(self.path_to_picture, basewidth)
        else:
            print("Can't load pictures for word:", self.word)


class Helper:
    @staticmethod
    def read_file_to_one_line(path):
        with open(path, 'r') as file:
            data = file.read()
            return data

    @staticmethod
    def translate(source, src='en', dest='ru'):
        translator = Translator()
        result = translator.translate(source, src=src, dest=dest)
        return result.text

    @staticmethod
    def get_random_id(string_length=10):
        letters = "123456789"
        result = ''.join(random.choice(letters) for i in range(string_length))
        return int(result)

    @staticmethod
    def get_import_file_name():
        return sys.argv[1]

    @staticmethod
    def save_speech_to(text_to_speech, subfolder, lang):
        speech = Speech(text_to_speech, lang)
        Helper.create_folder_if_not_exist(subfolder)
        path_to_save = subfolder + "\\" + text_to_speech + ".mp3"
        speech.save(path_to_save)
        return path_to_save

    @staticmethod
    def create_folder_if_not_exist(subfolder):
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
            print('Created subfolder:', subfolder)

    @staticmethod
    def load_pictures_to_download_subfolder(word, output_directory, count_of_pictures=1):
        file_names = []
        attempt_number = 1
        max_attempt_couter = 3
        while (len(file_names) < count_of_pictures):
            if (attempt_number > max_attempt_couter):
                break
            if (attempt_number > 1):
                print("Attempt to download <<", word, ">> image number", str(attempt_number))
            pic_downloader = google_images_download.googleimagesdownload()
            arguments = {"keywords": word, "limit": count_of_pictures, "silent_mode": 1,
                         "output_directory": output_directory}
            tuple_dict_err: Tuple[Dict[str, List[Any]], Union[int, Any]] = pic_downloader.download(arguments)
            error_count = tuple_dict_err[1]
            if (error_count == 0):
                dict_values: Dict[str, List[Any]] = tuple_dict_err[0]
                just_loaded = list(dict_values.values())[0]
                file_names += just_loaded
            attempt_number += 1
        return file_names

    @staticmethod
    def resize_image(path, basewidth):
        img = Image.open(path)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(path)

    @staticmethod
    def read_file_to_lines(file_name):
        import_lines = []
        with open(file_name, 'r') as reader:
            for line in reader.readlines():
                import_lines.append(line.rstrip())
        return import_lines


class Converter:
    def __init__(self):
        self.output_directory = "downloads"

    def start(self, file_path, export_dir):
        import_lines = Helper.read_file_to_lines(file_path)
        buckets = self.read_buckets(import_lines)
        file_name = os.path.basename(file_path)
        deck_name = file_name.rstrip(".txt")
        forward_manager = AnkiManager(deck_name)
        forward_manager.save_anki_package(buckets, export_dir + "\\" + deck_name + ".apkg")

        # remove temporary files
        for media_file in forward_manager.list_of_media_files:
            os.remove(media_file)

    def read_buckets(self, import_lines):
        buckets = []
        counter = 1
        bucket = Bucket()
        for line in import_lines:
            type_of_field = counter % 3
            if type_of_field == 1:
                bucket.word = line
            elif type_of_field == 2:
                bucket.meaning = line
            elif type_of_field == 0:
                bucket.example = line
                bucket.process(self.output_directory)
                buckets.append(bucket)
                bucket = Bucket()
            counter += 1
        return buckets


class AnkiManager:
    def __init__(self, deck_name):
        self.list_of_media_files = []
        self.model_id = Helper.get_random_id()
        self.deck_id = Helper.get_random_id()
        self.model_name = "marleeeeeey@gmail.com export"
        fields = [
            {'name': 'Word'},
            {'name': 'Image'},
            {'name': 'Sound'},
            {'name': 'Sound_Meaning'},
            {'name': 'Sound_Example'},
            {'name': 'Meaning'},
            {'name': 'Example'},
            {'name': 'IPA'},
            {'name': 'Word_Translation'},
            {'name': 'Meaning_Translation'},
            {'name': 'Example_Translation'},
        ]
        templates = [
            {
                'name': 'Card 1',
                'qfmt': Helper.read_file_to_one_line("anki_templates\\front_template.txt"),
                'afmt': Helper.read_file_to_one_line("anki_templates\\back_template.txt"),
            },
            {
                'name': 'Card 2',
                'qfmt': Helper.read_file_to_one_line("anki_templates\\front_template2.txt"),
                'afmt': Helper.read_file_to_one_line("anki_templates\\back_template2.txt"),
            },
        ]
        css = Helper.read_file_to_one_line("anki_templates\\css_template.txt")
        self.my_model = genanki.Model(self.model_id, self.model_name, fields=fields, templates=templates, css=css)
        self.my_deck = genanki.Deck(self.deck_id, deck_name)

    def save_anki_package(self, buckets, export_file_name):
        for bucket in buckets:
            self.add_bucket_to_deck(bucket)

        pack = genanki.Package(self.my_deck)
        pack.media_files = self.list_of_media_files
        Helper.create_folder_if_not_exist(os.path.dirname(export_file_name))
        pack.write_to_file(export_file_name)
        print("ANKI deck saved to", export_file_name)

    def add_bucket_to_deck(self, bucket):
        image_string = ""
        if (bucket.path_to_picture != ""):
            image_name = os.path.basename(bucket.path_to_picture)
            image_string = "<img src=\"" + image_name + "\">"
            self.list_of_media_files.append(bucket.path_to_picture)
        else:
            print("Image is not present for word:", bucket.word)
        word_sound_string = "[sound:" + os.path.basename(bucket.word_sound_path) + "]"
        meaning_sound_string = "[sound:" + os.path.basename(bucket.meaning_sound_path) + "]"
        self.list_of_media_files.append(bucket.word_sound_path)
        self.list_of_media_files.append(bucket.meaning_sound_path)
        note = genanki.Note(model=self.my_model,
                            fields=[bucket.word,
                                    image_string,
                                    word_sound_string,
                                    meaning_sound_string,
                                    "",  # Sound_Example
                                    bucket.meaning,
                                    bucket.example,
                                    "",  # IPA
                                    bucket.word_translation,
                                    bucket.meaning_translation,
                                    bucket.example_translation
                                    ])
        self.my_deck.add_note(note)


def main():
    converter = Converter()
    import_file_name = Helper.get_import_file_name()
    print("Processing file:", import_file_name)
    export_dir = "export"
    converter.start(import_file_name, export_dir)


main()
