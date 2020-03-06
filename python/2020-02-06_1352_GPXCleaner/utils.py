import glob
import xml.dom.minidom
from datetime import datetime as dt
import os.path


def get_file_list(mask):
    files = [f for f in glob.glob(mask, recursive=True)]
    return files


def xml_pretty(src, dest):
    dom = xml.dom.minidom.parse(src)
    pretty_xml_str = '\n'.join([line for line in dom.toprettyxml(indent=' ' * 2).split('\n') if line.strip()])
    with open(dest, "w", encoding="utf-8") as text_file:
        text_file.write(pretty_xml_str)

def get_pretty_time(raw_time_str):
    # input '2018-09-29T12:37:34Z'
    try:
        date_obj = dt.strptime(raw_time_str, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        date_obj = dt.strptime(raw_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    converted = dt.strftime(date_obj, '%Y-%m-%d_%H%M')
    return converted