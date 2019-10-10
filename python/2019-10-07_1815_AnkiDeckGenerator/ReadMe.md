# ANKI Deck Generator

## how to use it

1. Open list of words on [https://www.vocabulary.com](https://www.vocabulary.com/)

2. Select all lines and copy-paste them to text file.

   1. first line: word

   2. second line: meaning

   3. third line: example

   ![Example_web_page](Example_web_page.png)

   ![Example_Notepad](Example_Notepad.png)

3. Run python script: 

   ```
   anky_deck_generator.py <your_file_name>
   ```

4. Open `<your_file_name>.apkg` to import it to `ANKI`.

## Prerequisites

1. python 3.7
2. google_speech
3. googletrans
4. genanki
5. google_images_download (handmade 3rd party)