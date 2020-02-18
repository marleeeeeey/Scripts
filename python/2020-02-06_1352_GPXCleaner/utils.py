import glob
import xml.dom.minidom


def get_file_list(mask):
    files = [f for f in glob.glob(mask, recursive=True)]
    return files


def xml_pretty(src, dest):
    dom = xml.dom.minidom.parse(src)
    pretty_xml_str = '\n'.join([line for line in dom.toprettyxml(indent=' ' * 2).split('\n') if line.strip()])
    with open(dest, "w", encoding="utf-8") as text_file:
        text_file.write(pretty_xml_str)
