import argparse
import webbrowser
from weblib import WebTrackConverter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_url", type=str, required=True)
    parser.add_argument("-e", "--export_format", type=str, default = 'graphhopper', help="graphhopper/yandex/google")
    args = parser.parse_args()

    input_url = args.input_url
    track_converter = WebTrackConverter.create_instance(input_url)

    export_format = args.export_format
    if export_format == 'graphhopper':
        export_url = track_converter.export_url_graphhopper()
    else:
        raise Exception("Unknown type of export provider(url)")

    webbrowser.open(export_url)


main()
