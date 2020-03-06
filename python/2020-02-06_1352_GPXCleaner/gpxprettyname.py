import gpxlib
import argparse
import utils
from shutil import copyfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_glob_mask", type=str, required=True)
    parser.add_argument("-o", "--output_dir", type=str, default="./output/")
    args = parser.parse_args()
    gpx_files = utils.get_file_list(args.input_glob_mask)
    for gpx_file in gpx_files:
        pretty_name = gpxlib.get_pretty_name_from_gpx(gpx_file)
        copyfile(gpx_file, args.output_dir + pretty_name + '.gpx')

main()