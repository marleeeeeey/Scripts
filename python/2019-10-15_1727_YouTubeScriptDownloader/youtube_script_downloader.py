# pip install youtube_transcript_api
# pip install nltk

import youtube_transcript_api
import nltk.data
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import argparse


def init_nltk():
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def replace_break_line_with_space(msg):
    return msg.replace('\n', ' ').replace('\r', '')


def lines_to_one_line(lines):
    return_line = ""
    for line in lines:
        return_line += line + " "
    return return_line


def get_sentences_from_video(video_id, is_merge_screens):
    messages = []
    messages = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)
    lines = []
    print("Loaded", len(messages), "lines")
    for item in messages:
        text = item["text"]
        text = replace_break_line_with_space(text)
        if(not is_merge_screens):
            text += "\n"
        lines.append(text)
        # print(text)
    line = lines_to_one_line(lines)
    return split_line_on_sentences(line)


def split_line_on_sentences(line):
    nltk.download('punkt')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(line)


def append_lines_to_file(file_name, lines):
    with open(file_name, 'w', encoding="utf8") as the_file:
        for line in lines:
            the_file.write(line + '\n')


def parse_sentences_to_lemmas(sentences):
    lemmatizer = WordNetLemmatizer()
    for sentence in sentences:
        print(sentence)
        number = 0
        for w in nltk.word_tokenize(sentence):
            res = lemmatizer.lemmatize(w, get_wordnet_pos(w))
            print(str(number) + ') ' + res)
            number += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--merge", type=int,
                        help="Merge lines")
    parser.add_argument("-l", "--language", type=str, default="",
                        help="Language. For example: en-gb")
    parser.add_argument("-v", "--video", type=str, default="",
                        help="Video Id from YouTube. Example: MnT1xgZgkpk")
    parser.add_argument("-o", "--output", type=str, default="",
                        help="Output file name")
    args = parser.parse_args()
    init_nltk()
    video_id = args.video
    is_merge_screens = args.merge
    sentences = get_sentences_from_video(video_id, is_merge_screens)
    output_file = args.output
    append_lines_to_file(output_file, sentences)
    return


main()
