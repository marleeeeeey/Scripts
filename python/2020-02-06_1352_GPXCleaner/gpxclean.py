import argparse
import ntpath
import os
import sys

import gpxlib
import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", type=str, default="./output/")
    parser.add_argument("-t", "--ignore_time", action='store_true')
    parser.add_argument("-e", "--ignore_elevation", action='store_true')
    parser.add_argument("-d", "--ignore_metadata", action='store_true')
    parser.add_argument("-r", "--replace_original", action='store_true')
    parser.add_argument("-w", "--ignore_wpt", action='store_true')
    parser.add_argument("-m", "--merge_tracks", action='store_true')
    parser.add_argument("-n", "--auto_rename", action='store_true')
    parser.add_argument('gpx_files', nargs='*')
    args = parser.parse_args()

    gpx_files = []
    if not args.gpx_files:
        for line in sys.stdin:
            line = line.strip('\n')
            gpx_files.append(line)
    else:
        gpx_files = args.gpx_files
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
            if args.auto_rename:
                gpxlib.gpx_auto_rename(export_gpx)
        except:
            print("Can't parse file: ", base_name)


main()
