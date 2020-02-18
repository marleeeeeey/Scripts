import argparse
import ntpath
import os

import gpxlib
import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_glob_mask", type=str, required=True, help="Input glob mask")
    parser.add_argument("-o", "--output_dir", type=str, default="./output/", help="Output directory")
    parser.add_argument("-t", "--ignore_time", action='store_true')
    parser.add_argument("-e", "--ignore_elevation", action='store_true')
    parser.add_argument("-d", "--ignore_metadata", action='store_true')
    parser.add_argument("-r", "--replace_original", action='store_true')
    parser.add_argument("-w", "--ignore_wpt", action='store_true')
    parser.add_argument("-m", "--merge_tracks", action='store_true')
    args = parser.parse_args()

    gpx_files = utils.get_file_list(args.input_glob_mask)
    print('file count:', len(gpx_files))

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for src_gpx in gpx_files:
        base_name = ntpath.basename(src_gpx)
        export_gpx = output_dir + base_name
        if args.replace_original:
            export_gpx = src_gpx
        try:
            gpxlib.gpx_cleaner(src_gpx, export_gpx, args.merge_tracks, args.ignore_wpt,
                               args.ignore_metadata, args.ignore_time, args.ignore_elevation)
        except:
            print("Can't parse file: ", base_name)


main()
