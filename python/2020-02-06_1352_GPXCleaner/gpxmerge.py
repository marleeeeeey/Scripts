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
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    files = []

    if not args.files:
        for line in sys.stdin:
            line = line.strip('\n')
            files.append(line)
    else:
        files = args.files

    print('file count:', len(files))

    if len(files) < 1:
        return

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = ntpath.basename(files[0])
    export_gpx = output_dir + base_name
    export_tree = gpxlib.get_merge_gpx_tree(files, args.merge_tracks, args.ignore_wpt)
    gpxlib.write_gpxtree(export_tree, export_gpx)
    print('Done. Merged',len(files),'file(s)')


main()
