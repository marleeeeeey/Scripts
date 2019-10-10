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
        self.path_to_sound = ""
        self.meaning = ""
        self.meaning_translation = ""
        self.example = ""
        self.example_translation = ""
        self.path_to_picture = ""
        self.isPictureLoaded = True

    def print(self):
        print(" word:", self.word, "\n",
              "word_translation:", self.word_translation, "\n",
              "path_to_sound:", self.path_to_sound, "\n",
              "meaning:", self.meaning, "\n",
              "meaning_translation:", self.meaning_translation, "\n",
              "example:", self.example, "\n",
              "example_translation:", self.example_translation, "\n",
              "path_to_picture:", self.path_to_picture)

    def process(self):
        self.generate_translations()
        self.generate_speech()
        try:
            self.generate_pictures()
        except AttributeError:
            print("can't generate image", self.word)

    def generate_translations(self):
        self.example_translation = Helper.translate(self.example)
        self.meaning_translation = Helper.translate(self.meaning)
        self.word_translation = Helper.translate(self.word)

    def generate_speech(self):
        speech = Speech(self.word, "en")
        self.path_to_sound = self.word + ".mp3"
        speech.save(self.path_to_sound)

    def generate_pictures(self):
        count_of_pictures = 1  # TODO
        basewidth = 300
        pictures = Helper.load_pictures(self.word, count_of_pictures)
        if(len(pictures) != 0):
            self.path_to_picture = pictures[0]
            Helper.resize_image(self.path_to_picture, basewidth)
        else:
            print("Can't load pictures for word:", self.word)
            self.isPictureLoaded = False


class Helper:
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
    def load_pictures(word, count_of_pictures=1):
        file_names = []
        attempt_number = 1
        max_attempt_couter = 3
        while(len(file_names) < count_of_pictures):
            if(attempt_number > max_attempt_couter):
                break
            if(attempt_number > 1):
                print("attemt to dowload <<", word, ">> image number", str(attempt_number))
            pic_downloader = google_images_download.googleimagesdownload()
            arguments = {"keywords": word, "limit": count_of_pictures, "silent_mode": 1 }
            tuple_dict_err: Tuple[Dict[str, List[Any]], Union[int, Any]] = pic_downloader.download(arguments)
            error_count = tuple_dict_err[1]
            if(error_count == 0):
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


class Converter:
    def start(self, import_file_name):
        import_lines = self.read_lines(import_file_name)
        buckets = self.read_buckets(import_lines)
        deck_name = import_file_name.rstrip(".txt")

        forward_manager = AnkiManager(deck_name)
        forward_manager.save_anki_package(buckets, deck_name + ".apkg")

        # remove temporary files
        for media_file in forward_manager.list_of_media_files:
            os.remove(media_file)

    def read_lines(self, import_file_name):
        import_lines = []
        with open(import_file_name, 'r') as reader:
            for line in reader.readlines():
                import_lines.append(line.rstrip())
        return import_lines

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
                bucket.process()
                #bucket.print()
                buckets.append(bucket)
                bucket = Bucket()
            counter += 1
        print("Processed", len(buckets), "words")
        return buckets


class AnkiManager:
    def print(self):
        print("model_id=", self.model_id)
        print("deck_id =", self.deck_id)

    def __init__(self, deck_name):
        self.list_of_media_files = []
        self.model_id = Helper.get_random_id()
        self.deck_id = Helper.get_random_id()
        self.model_name = "marleeeeeey@gmail.com export"
        fields = [
            {'name': 'Question'},
            {'name': 'BWQuestion'},
            {'name': 'Answer'},
            {'name': 'BWAnswer'},
            {'name': 'Sound'},
            {'name': 'Picture'},
        ]
        templates = [
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}<br>{{Sound}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>{{Picture}}<br>{{Sound}}',
            },
            {
                'name': 'Card 2',
                'qfmt': '{{BWQuestion}}<br>{{Picture}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{BWAnswer}}<br>{{Sound}}',
            },
        ]
        self.my_model = genanki.Model(self.model_id, self.model_name, fields = fields, templates=templates)
        self.my_deck = genanki.Deck(self.deck_id, deck_name)

    def get_forward_template(self):
        return

    def save_anki_package(self, buckets, export_file_name):
        for bucket in buckets:
            if(bucket.isPictureLoaded == False):
                continue
            question = bucket.word + "<br><br>" + bucket.example
            backward_question = bucket.word_translation
            answer = bucket.word + "<br>" + \
                     bucket.word_translation + "<br><br>" + \
                     bucket.meaning + "<br>" + \
                     bucket.meaning_translation + "<br><br>" + \
                     bucket.example + "<br>" + \
                     bucket.example_translation
            backward_answer = answer
            sound_string = "[sound:" + bucket.path_to_sound + "]"
            image_name = os.path.basename(bucket.path_to_picture)
            image_string = "<img src=\"" + image_name + "\">"
            print(image_string)
            self.list_of_media_files.append(bucket.path_to_sound)
            self.list_of_media_files.append(bucket.path_to_picture)
            note = genanki.Note(model=self.my_model,
                                fields=[question, backward_question,
                                        answer, backward_answer,
                                        sound_string, image_string])
            self.my_deck.add_note(note)
        pack = genanki.Package(self.my_deck)
        pack.media_files = self.list_of_media_files
        pack.write_to_file(export_file_name)
        print("ANKI deck saved to", export_file_name)


def main():
    converter = Converter()
    import_file_name = Helper.get_import_file_name()
    print("Import file name is", import_file_name)
    converter.start(import_file_name)


main()
