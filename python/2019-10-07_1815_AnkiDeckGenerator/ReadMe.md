# ANKI Deck Generator

## Description

This script can generate Anki cards from list of words. The list can contain different formats of data:
 
 1. **Type 00**: one line equal one word.
 2. **Type 01**: three lines in the next order: word, meaning, example.
 3. **Type 02**: two lines in the next order: word, translation.
 4. **Type 03**: two lines in the next order: word, meaning.

Word translation and pronunciation will be generated for all types.

## How to use it

1. Prepare the text file according to the type described above.
2. Run python script: 
   ```
   anky_deck_generator.py -t <FileType> -i <input_file_name>
   ```
4. Anki deck will generate in `export` folder.

## Prerequisites

1. python 3.7
2. google_speech
3. googletrans
4. genanki
5. google_images_download
