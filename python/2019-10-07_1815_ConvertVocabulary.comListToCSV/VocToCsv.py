import sys
from googletrans import Translator
import genanki
from google_speech import Speech
import os
import random

# defines
class Bucket:
    def __init__(self):
        self.word = ""
        self.word_translation = ""
        self.meaning = ""
        self.example = ""
        self.example_translation = ""
        self.path_to_sound = ""

def translate(source):
    translator = Translator()
    result = translator.translate(source , src='en', dest='ru')
    return result.text
    
def print_bucket(b):
    print(" word:", b.word, "\n", "meaning:", b.meaning, "\n",
        "example:", b.example, "\n", "example_translation:", b.example_translation, "\n")

def randomId(stringLength=10):
    letters = "123456789"
    result = ''.join(random.choice(letters) for i in range(stringLength))
    return int(result)
    
# parse args
importFileName = sys.argv[1]
print("importFileName=", importFileName)
exportFileName = importFileName + "_export.apkg"
print("exportFileName=", exportFileName)

# read to list of lines
importArray = []
with open(importFileName, 'r') as reader:
     for line in reader.readlines():        
        importArray.append(line.rstrip())

# convert to list of Buckets
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
        buckets.append(bucket)
        bucket = Bucket()
    counter += 1


# updated list of audio files        
# add translate and path to audio
list_of_audio_files = []
for bucket in buckets:
    bucket.example_translation = translate(bucket.example)      
    bucket.word_translation = translate(bucket.word)  
    speech = Speech(bucket.word, "en");
    sound_name = bucket.word+".mp3"
    speech.save(sound_name)
    bucket.path_to_sound = sound_name
    list_of_audio_files.append(sound_name)
    print_bucket(bucket)


# anki defaults
model_id = randomId()
deck_id  = randomId()

print("model_id=", model_id)
print("deck_id =", deck_id)

my_model = genanki.Model(
  model_id,
  'https://www.vocabulary.com export',
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

my_deck = genanki.Deck(
    deck_id,
    importFileName
)

#export to anki
for bucket in buckets:
    first_side = bucket.word + "<br><br>" + bucket.example
    second_side = bucket.word_translation + "<br><br>" + bucket.example_translation + "<br><br>" + bucket.meaning;
    sound_string = "[sound:" + bucket.path_to_sound + "]"
    note = genanki.Note(model=my_model,fields=[first_side, second_side, sound_string])
    my_deck.add_note(note)
pack = genanki.Package(my_deck)
pack.media_files = list_of_audio_files
pack.write_to_file(exportFileName)

# remove temporary files
for media_file in list_of_audio_files:
    os.remove(media_file)
    