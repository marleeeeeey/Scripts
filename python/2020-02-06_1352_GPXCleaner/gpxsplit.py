import argparse
import os

import gpxlib
import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_glob_mask", type=str, default="./", help="Input glob mask")
    parser.add_argument("-o", "--output_dir", type=str, default="./output/", help="Output directory")
    args = parser.parse_args()

    gpx_files = utils.get_file_list(args.input_glob_mask)
    print('file count:', len(gpx_files))

    if len(gpx_files) < 1:
        return

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for gpx in gpx_files:
        gpxlib.split_gpx(gpx, output_dir)


main()
