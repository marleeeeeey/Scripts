from google_images_download import google_images_download
from typing import Dict, List, Any, Tuple, Union
import argparse


def load_pictures(word, output_folder, count_of_pictures=1):
    file_names = []
    attempt_number = 1
    max_attempt_couter = 3
    while len(file_names) < count_of_pictures:
        if attempt_number > max_attempt_couter:
            break
        if attempt_number > 1:
            print("Attempt to download <<", word, ">> image number", str(attempt_number))
        pic_downloader = google_images_download.googleimagesdownload()
        arguments = {"keywords": word,
                     "limit": count_of_pictures,
                     "silent_mode": 1,
                     "output_directory": output_folder}
        tuple_dict_err: Tuple[Dict[str, List[Any]], Union[int, Any]] = pic_downloader.download(arguments)
        error_count = tuple_dict_err[1]
        if error_count == 0:
            dict_values: Dict[str, List[Any]] = tuple_dict_err[0]
            just_loaded = list(dict_values.values())[0]
            file_names += just_loaded
        attempt_number += 1
    return file_names


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--words", type=str, default="", help="List of words to find images")
    parser.add_argument("-c", "--count", type=int, default=1, help="Count images of every word")
    parser.add_argument("-o", "--output", type=str, default="output", help="Count images of every word")
    args = parser.parse_args()

    words = args.words.split()
    pic_numbers = args.count
    output_folder = args.output
    counter = 0

    for word in words:
        pictures_array = load_pictures(word, output_folder, pic_numbers)
        counter += len(pictures_array)

    print("Summary: Loaded", counter, "pictures")


main()
