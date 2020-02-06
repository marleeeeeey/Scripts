import xml.etree.ElementTree as ET
import os
import ntpath
import argparse
import glob


def get_default_ns():
    return "http://www.topografix.com/GPX/1/1"


def get_gpx_file_list(glob_expression):
    files = [f for f in glob.glob(glob_expression, recursive=True)]
    return files


def wrap_default_namespace(str):
    full_name = '{' + get_default_ns()+ '}' + str
    return full_name


def remove_wpt_items(src, dest):
    ET.register_namespace('', get_default_ns())
    tree = ET.parse(src)
    root = tree.getroot()
    new_root = ET.Element(root.tag)
    new_root.set('version', root.attrib['version'])
    new_root.set('creator', "marleeeeeey@gmail.com")
    new_tree = ET.ElementTree(new_root)

    for child in root:
        if child.tag == wrap_default_namespace('metadata'):
            new_root.append(child)

    # move several tracks into one. Segments are keep.
    one_trk = ET.SubElement(new_root, 'trk')
    for trk in root.findall(wrap_default_namespace('trk')):
        one_trkseg = ET.SubElement(one_trk, 'trkseg')
        for trkseg in trk.findall(wrap_default_namespace('trkseg')):
            for trkpt in trkseg.findall(wrap_default_namespace('trkpt')):
                new_trkpt = ET.SubElement(one_trkseg, 'trkpt', trkpt.attrib)

    new_tree.write(dest, xml_declaration=True, encoding='utf-8', method="xml")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_dir", type=str, default="./", help="Input directory")
    parser.add_argument("-o", "--output_dir", type=str, default="./output/", help="Output directory")
    args = parser.parse_args()

    gpx_files = get_gpx_file_list(args.input_dir)
    print('found files:', gpx_files)
    print('file count:', len(gpx_files))

    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for gpx_file in gpx_files:
        base_name = ntpath.basename(gpx_file)
        export_path = output_dir + base_name
        try:
            remove_wpt_items(gpx_file, export_path)
        except ET.ParseError:
            print("Can't parse file: ", base_name)

main()
