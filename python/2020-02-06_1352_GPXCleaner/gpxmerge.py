import argparse
import ntpath
import os

import gpxlib
import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_glob_mask", type=str, required=True)
    parser.add_argument("-o", "--output_dir", type=str, default="./output/")
    parser.add_argument("-w", "--ignore_wpt", action='store_true')
    parser.add_argument("-m", "--merge_tracks", action='store_true')
    args = parser.parse_args()

    gpx_files = utils.get_file_list(args.input_glob_mask)
    print('file count:', len(gpx_files))

    if len(gpx_files) < 1:
        return

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = ntpath.basename(gpx_files[0])
    export_gpx = output_dir + base_name
    export_tree = gpxlib.get_merge_gpx_tree(gpx_files, args.merge_tracks, args.ignore_wpt)
    gpxlib.write_gpxtree(export_tree, export_gpx)


main()
