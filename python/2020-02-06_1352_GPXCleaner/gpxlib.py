import glob
import xml.dom.minidom
import xml.etree.ElementTree as ET


def get_default_ns():
    return "http://www.topografix.com/GPX/1/1"


def get_file_list(mask):
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


def copy_track(src_root, dest_root, merge_tracks = False, ignore_time = False, ignore_elevation = False):
    trks = src_root.findall(wrap_default_namespace('trk'))
    if(len(trks) == 0):
        return

    if merge_tracks:
        _copy_track_and_merge_as_segments(src_root, dest_root, ignore_time, ignore_elevation)
        return

    for trk in trks:
        one_trk = ET.SubElement(dest_root, 'trk')
        for trkseg in trk.findall(wrap_default_namespace('trkseg')):
            one_trkseg = ET.SubElement(one_trk, 'trkseg')
            for trkpt in trkseg.findall(wrap_default_namespace('trkpt')):
                new_trkpt = ET.SubElement(one_trkseg, 'trkpt', trkpt.attrib)
                for child in trkpt:
                    if child.tag == wrap_default_namespace('time') and not ignore_time:
                        new_trkpt.append(child)
                    if child.tag == wrap_default_namespace('ele') and not ignore_elevation:
                        new_trkpt.append(child)


def _copy_track_and_merge_as_segments(src_root, dest_root, ignore_time, ignore_elevation):
    trks = src_root.findall(wrap_default_namespace('trk'))
    if(len(trks) == 0):
        return
    one_trk = ET.SubElement(dest_root, 'trk')
    for trk in trks:
        one_trkseg = ET.SubElement(one_trk, 'trkseg')
        for trkseg in trk.findall(wrap_default_namespace('trkseg')):
            for trkpt in trkseg.findall(wrap_default_namespace('trkpt')):
                new_trkpt = ET.SubElement(one_trkseg, 'trkpt', trkpt.attrib)
                for child in trkpt:
                    if child.tag == wrap_default_namespace('time') and not ignore_time:
                        new_trkpt.append(child)
                    if child.tag == wrap_default_namespace('ele') and not ignore_elevation:
                        new_trkpt.append(child)


def copy_metadata(src_root, dest_root):
    for metadata in src_root.findall(wrap_default_namespace('metadata')):
        new_metadata = ET.SubElement(dest_root, 'metadata', metadata.attrib)
        for child in metadata:
            if child.tag == wrap_default_namespace('name'):
                new_metadata.append(child)


def copy_wpt(src_root, dest_root):
    for wpt in src_root.findall(wrap_default_namespace('wpt')):
        new_wpt = ET.SubElement(dest_root, 'wpt', wpt.attrib)
        for child in wpt:
            if child.tag == wrap_default_namespace('name') or child.tag == wrap_default_namespace('time'):
                new_wpt.append(child)


def write_gpxtree(tree, dest):
    tree.write(dest, xml_declaration=True, encoding='utf-8', method="xml")
    xml_pretty(dest, dest)


def gpx_cleaner(src, dest, merge_tracks = False, ignore_metadata = False, ignore_time = False, ignore_elevation = False):
    tree = ET.parse(src)
    root = tree.getroot()
    new_tree = create_empty_gpx_tree(root)
    new_root = new_tree.getroot()
    if not ignore_metadata:
        copy_metadata(root, new_root)
    copy_wpt(root, new_root)
    copy_track(root, new_root, merge_tracks, ignore_time, ignore_elevation)
    write_gpxtree(new_tree, dest)


def get_merge_gpx_tree(gpx_files, merge_tracks = False):
    main_tree = ET.parse(gpx_files[0])
    main_root = main_tree.getroot()
    new_tree = create_empty_gpx_tree(main_root)
    new_root = new_tree.getroot()
    copy_metadata(main_root, new_root)
    for gpx in gpx_files:
        tree = ET.parse(gpx)
        root = tree.getroot()
        copy_wpt(root, new_root)
    for gpx in gpx_files:
        tree = ET.parse(gpx)
        root = tree.getroot()
        copy_track(root, new_root, merge_tracks)
    return new_tree
