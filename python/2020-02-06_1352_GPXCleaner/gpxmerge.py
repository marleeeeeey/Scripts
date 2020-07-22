import argparse
import ntpath
import os

import sys
import gpxlib


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", type=str, default="./output/")
    parser.add_argument("-w", "--ignore_wpt", action='store_true')
    parser.add_argument("-m", "--merge_tracks", action='store_true')
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

    if len(gpx_files) < 1:
        return

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = ntpath.basename(gpx_files[0])
    export_gpx = output_dir + base_name
    export_tree = gpxlib.get_merge_gpx_tree(gpx_files, args.merge_tracks, args.ignore_wpt)
    gpxlib.write_gpxtree(export_tree, export_gpx)
    print('Done. Merged',len(gpx_files),'file(s)')


main()
