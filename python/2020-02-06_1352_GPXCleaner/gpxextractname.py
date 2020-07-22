import argparse
import os
import sys
from shutil import copyfile

import gpxlib
import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", type=str, default="./output/")
    parser.add_argument("-t", "--retrieve_time", action='store_true')
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

    for gpx_file in gpx_files:
        pretty_name = gpxlib.get_pretty_name_from_gpx(gpx_file, args.retrieve_time)
        pretty_name.replace('.gpx', '')
        copyfile(gpx_file, args.output_dir + pretty_name + '.gpx')


main()
