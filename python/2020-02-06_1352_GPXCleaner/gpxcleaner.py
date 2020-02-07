import argparse
import glob
import ntpath
import os
import xml.dom.minidom
import xml.etree.ElementTree as ET


def get_default_ns():
    return "http://www.topografix.com/GPX/1/1"


def get_gpx_file_list(mask):
    files = [f for f in glob.glob(mask, recursive=True)]
    return files


def wrap_default_namespace(tag):
    full_name = '{' + get_default_ns() + '}' + tag
    return full_name


def create_empty_gpx_tree(root):
    ET.register_namespace('', get_default_ns())
    new_root = ET.Element(root.tag)
    new_root.set('version', root.attrib['version'])
    new_root.set('creator', "marleeeeeey@gmail.com")
    new_tree = ET.ElementTree(new_root)
    return new_tree


def xml_pretty(src, dest):
    dom = xml.dom.minidom.parse(src)
    pretty_xml_str = '\n'.join([line for line in dom.toprettyxml(indent=' ' * 2).split('\n') if line.strip()])
    with open(dest, "w", encoding="utf-8") as text_file:
        text_file.write(pretty_xml_str)


def convert_gpx(src, dest, args):
    tree = ET.parse(src)
    root = tree.getroot()
    new_tree = create_empty_gpx_tree(root)
    new_root = new_tree.getroot()
    # copy name from metadata
    if not args.ignore_metadata:
        for metadata in root.findall(wrap_default_namespace('metadata')):
            new_metadata = ET.SubElement(new_root, 'metadata', metadata.attrib)
            for child in metadata:
                if child.tag == wrap_default_namespace('name'):
                    new_metadata.append(child)
    # copy wpt's
    for wpt in root.findall(wrap_default_namespace('wpt')):
        new_wpt = ET.SubElement(new_root, 'wpt', wpt.attrib)
        for child in wpt:
            if child.tag == wrap_default_namespace('name'):
                new_wpt.append(child)
    # move several tracks into one. Segments are keep.
    one_trk = ET.SubElement(new_root, 'trk')
    for trk in root.findall(wrap_default_namespace('trk')):
        one_trkseg = ET.SubElement(one_trk, 'trkseg')
        for trkseg in trk.findall(wrap_default_namespace('trkseg')):
            for trkpt in trkseg.findall(wrap_default_namespace('trkpt')):
                new_trkpt = ET.SubElement(one_trkseg, 'trkpt', trkpt.attrib)
                # keep elevation and time
                for child in trkpt:
                    if child.tag == wrap_default_namespace('time') and not args.ignore_time:
                        new_trkpt.append(child)
                    if child.tag == wrap_default_namespace('ele') and not args.ignore_elevation:
                        new_trkpt.append(child)
    # write to destination
    new_tree.write(dest, xml_declaration=True, encoding='utf-8', method="xml")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_glob_mask", type=str, default="./", help="Input glob mask")
    parser.add_argument("--ignore_time", action='store_true')
    parser.add_argument("--ignore_elevation", action='store_true')
    parser.add_argument("--ignore_metadata", action='store_true')
    parser.add_argument("-o", "--output_dir", type=str, default="./output/", help="Output directory")
    args = parser.parse_args()

    gpx_files = get_gpx_file_list(args.input_glob_mask)
    print('found files:', gpx_files)
    print('file count:', len(gpx_files))

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for src_gpx in gpx_files:
        base_name = ntpath.basename(src_gpx)
        export_gpx = output_dir + base_name
        try:
            convert_gpx(src_gpx, export_gpx, args)
            xml_pretty(export_gpx, export_gpx)
        except ET.ParseError:
            print("Can't parse file: ", base_name)


main()
