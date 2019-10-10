import sys
from googletrans import Translator
import genanki
from google_speech import Speech
import os
import random


class Bucket:
    def __init__(self):
        self.word = ""
        self.word_translation = ""
        self.path_to_sound = ""
        self.meaning = ""
        self.meaning_translation = ""
        self.example = ""
        self.example_translation = ""

    def print(self):
        print(" word:", self.word, "\n",
              "meaning:", self.meaning, "\n",
              "example:", self.example, "\n",
              "example_translation:", self.example_translation)

    def process(self):
        print("Processing word:", self.word)
        self.generate_translations()
        self.generate_speech()

    def generate_translations(self):
        self.example_translation = Helper.translate(self.example)
        self.meaning_translation = Helper.translate(self.meaning)
        self.word_translation = Helper.translate(self.word)

    def generate_speech(self):
        speech = Speech(self.word, "en")
        self.path_to_sound = self.word + ".mp3"
        speech.save(self.path_to_sound)

    def generate_picture(self):
        # todo
        return


class Helper:
    @staticmethod
    def translate(source, src='en', dest='ru'):
        translator = Translator()
        result = translator.translate(source, src, dest)
        return result.text

    @staticmethod
    def get_random_id(stringLength=10):
        letters = "123456789"
        result = ''.join(random.choice(letters) for i in range(stringLength))
        return int(result)

    @staticmethod
    def get_import_file_name():
        return sys.argv[1]


class Converter:
    def start(self, import_file_name):
        importArray = self.read_lines(import_file_name)
        buckets = self.read_buckets(importArray)
        deck_name = import_file_name.rstrip(".txt")
        anki_manager = AnkiManager(deck_name)
        export_file_name = deck_name + ".apkg"
        anki_manager.save_anki_package(buckets, export_file_name)

    def read_lines(self, import_file_name):
        importArray = []
        with open(import_file_name, 'r') as reader:
            for line in reader.readlines():
                importArray.append(line.rstrip())
        return importArray

    def read_buckets(self, importArray):
        buckets = []
        counter = 1
        bucket = Bucket()
        for line in importArray:
            type = counter % 3
            if type == 1:
                bucket.word = line
            elif type == 2:
                bucket.meaning = line
            elif type == 0:
                bucket.example = line
                bucket.process()
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
        self.model_id = Helper.get_random_id()
        self.deck_id = Helper.get_random_id()
        self.model_name = "marleeeeeey@gmail.com export"
        self.my_model = genanki.Model(
            self.model_id,
            self.model_name,
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
                {'name': 'MyMedia'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Question}}<br>{{MyMedia}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ])
        self.my_deck = genanki.Deck(self.deck_id, deck_name)

    def save_anki_package(self, buckets, export_file_name):
        list_of_audio_files = []
        for bucket in buckets:
            first_side = bucket.word + "<br><br>" + bucket.example
            second_side = bucket.word_translation + "<br><br>" + \
                          bucket.meaning + "<br>" + \
                          bucket.meaning_translation + "<br><br>" + \
                          bucket.example + "<br>" + \
                          bucket.example_translation
            sound_string = "[sound:" + bucket.path_to_sound + "]"
            list_of_audio_files.append(bucket.path_to_sound)
            note = genanki.Note(model=self.my_model, fields=[first_side, second_side, sound_string])
            self.my_deck.add_note(note)
        pack = genanki.Package(self.my_deck)
        pack.media_files = list_of_audio_files
        pack.write_to_file(export_file_name)
        print("ANKI deck saved to", export_file_name)
        # remove temporary files
        for media_file in list_of_audio_files:
            os.remove(media_file)

# main
converter = Converter()
import_file_name = Helper.get_import_file_name()
print("Import file name is", import_file_name)
converter.start(import_file_name)
