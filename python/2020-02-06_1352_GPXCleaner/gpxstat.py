import argparse
import ntpath
import os

import gpxlib
import utils

from shutil import copyfile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_glob_mask", type=str, required=True)
    parser.add_argument("-o", "--output_dir", type=str, default="./output/")
    args = parser.parse_args()

    gpx_files = utils.get_file_list(args.input_glob_mask)
    print('file count:', len(gpx_files))

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for src_gpx in gpx_files:
        track_count = gpxlib.get_track_count(src_gpx)
        if(track_count > 1):
            print(src_gpx, "count=", track_count)
            base_name = ntpath.basename(src_gpx)
            export_gpx = output_dir + base_name
            copyfile(src_gpx, export_gpx)


main()
