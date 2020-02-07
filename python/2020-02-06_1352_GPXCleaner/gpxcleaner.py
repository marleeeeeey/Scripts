import gpxlib
import argparse
import ntpath
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_glob_mask", type=str, default="./", help="Input glob mask")
    parser.add_argument("--ignore_time", action='store_true')
    parser.add_argument("--ignore_elevation", action='store_true')
    parser.add_argument("--ignore_metadata", action='store_true')
    parser.add_argument("--replace_original", action='store_true')
    parser.add_argument("-o", "--output_dir", type=str, default="./output/", help="Output directory")
    args = parser.parse_args()

    gpx_files = gpxlib.get_file_list(args.input_glob_mask)
    print('found files:', gpx_files)
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
            ignore_metadata = args.ignore_metadata
            ignore_time = args.ignore_time
            ignore_elevation = args.ignore_elevation
            gpxlib.gpx_cleaner(src_gpx, export_gpx, ignore_metadata, ignore_time, ignore_elevation)
        except:
            print("Can't parse file: ", base_name)


main()
