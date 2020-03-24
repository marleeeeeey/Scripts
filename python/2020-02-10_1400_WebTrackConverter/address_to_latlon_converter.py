import argparse
import webbrowser
from weblib import WebTrackConverter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_addresses", type=str, required=True)
    parser.add_argument("-e", "--export_format", type=str, default = 'graphhopper', help="graphhopper/yandex/google")
    args = parser.parse_args()

    input_addresses = args.input_addresses
    list_of_addresses = input_addresses.split('-')
    trimmed_list_of_addresses = []
    for address in list_of_addresses:
        trimmed_list_of_addresses.append(address.strip())
    print('found addresses:', trimmed_list_of_addresses)
    track_converter = WebTrackConverter.create_instance_from_list_of_addresses("Москва", trimmed_list_of_addresses)

    export_format = args.export_format
    if export_format == 'graphhopper':
        export_url = track_converter.export_url_graphhopper()
    else:
        raise Exception("Unknown type of export provider(url)")

    webbrowser.open(export_url)

main()