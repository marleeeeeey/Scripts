import ntpath
import os
import xml.etree.ElementTree as ET

import utils


def get_default_ns():
    return "http://www.topografix.com/GPX/1/1"


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


def copy_track(src_root, dest_root, merge_tracks=False, ignore_time=False, ignore_elevation=False, desired_name=None):
    trks = src_root.findall(wrap_default_namespace('trk'))
    if (len(trks) == 0):
        return

    if merge_tracks:
        one_trk = ET.SubElement(dest_root, 'trk')
        for trk in trks:
            for trkseg in trk.findall(wrap_default_namespace('trkseg')):
                new_trkseg = ET.SubElement(one_trk, 'trkseg')
                copy_trkseg(trkseg, new_trkseg, ignore_time, ignore_elevation)
    else:
        for trk in trks:
            dest_trk = ET.SubElement(dest_root, 'trk')
            dest_trk_name = ET.SubElement(dest_trk, 'name')
            src_track_name = get_track_name(trk)
            if src_track_name != None:
                dest_trk_name.text = src_track_name.replace(".gpx", "")
            elif desired_name != None:
                dest_trk_name.text = desired_name
            for trkseg in trk.findall(wrap_default_namespace('trkseg')):
                dest_trkseg = ET.SubElement(dest_trk, 'trkseg')
                copy_trkseg(trkseg, dest_trkseg, ignore_time, ignore_elevation)


def copy_trkseg(src_trkseg, dest_trkseg, ignore_time=False, ignore_elevation=False):
    for trkpt in src_trkseg.findall(wrap_default_namespace('trkpt')):
        new_trkpt = ET.SubElement(dest_trkseg, 'trkpt', trkpt.attrib)
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
    utils.xml_pretty(dest, dest)


def gpx_cleaner(src, dest, merge_tracks=False, ignore_wpt=False, ignore_metadata=False, ignore_time=False,
                ignore_elevation=False):
    tree = ET.parse(src)
    root = tree.getroot()
    new_tree = create_empty_gpx_tree(root)
    new_root = new_tree.getroot()
    if not ignore_metadata:
        copy_metadata(root, new_root)
    if not ignore_wpt:
        copy_wpt(root, new_root)
    copy_track(root, new_root, merge_tracks, ignore_time, ignore_elevation)
    write_gpxtree(new_tree, dest)


def get_merge_gpx_tree(gpx_files, merge_tracks=False, ignore_wpt=False):
    main_tree = ET.parse(gpx_files[0])
    main_root = main_tree.getroot()
    new_tree = create_empty_gpx_tree(main_root)
    new_root = new_tree.getroot()
    copy_metadata(main_root, new_root)
    if not ignore_wpt:
        for gpx in gpx_files:
            tree = ET.parse(gpx)
            root = tree.getroot()
            copy_wpt(root, new_root)
    for gpx in gpx_files:
        tree = ET.parse(gpx)
        root = tree.getroot()
        copy_track(root, new_root, merge_tracks, desired_name=ntpath.basename(gpx))
    return new_tree


def split_gpx(gpx, output_dir):
    tree = ET.parse(gpx)
    root = tree.getroot()
    full_name = ntpath.basename(gpx)
    name_wihtout_ext = os.path.splitext(full_name)[0]
    extension = os.path.splitext(full_name)[1]

    trks = root.findall(wrap_default_namespace('trk'))
    if (len(trks) == 0):
        return

    index = 0
    for trk in trks:
        new_tree = create_empty_gpx_tree(root)
        new_root = new_tree.getroot()
        new_metadata = ET.SubElement(new_root, 'metadata')
        new_metadata_name = ET.SubElement(new_metadata, 'name')
        track_name = get_track_name(trk)
        new_metadata_name.text = track_name
        new_trk = ET.SubElement(new_root, 'trk')
        new_track_name = ET.SubElement(new_trk, 'name')
        new_track_name.text = track_name
        for trkseg in trk.findall(wrap_default_namespace('trkseg')):
            dest_trkseg = ET.SubElement(new_trk, 'trkseg')
            copy_trkseg(trkseg, dest_trkseg)

        file_name = output_dir + str(index) + '_' + track_name + extension
        write_gpxtree(new_tree, file_name)
        index += 1


def get_track_count(gpx_file_name):
    tree = ET.parse(gpx_file_name)
    root = tree.getroot()
    counter = 0
    for trk in root.findall(wrap_default_namespace('trk')):
        counter += 1
    return counter


def remove_special_symbols(track_name):
    track_name = track_name.replace(':', '')
    track_name = track_name.replace('/', '')
    track_name = track_name.replace('_', ' ')
    return track_name


def get_track_name(trk):
    trk_name_obj = trk.find(wrap_default_namespace('name'))
    if trk_name_obj != None:
        return remove_special_symbols(trk_name_obj.text)
    else:
        return None


def get_pretty_name_from_gpx(gpx_file_name):
    tree = ET.parse(gpx_file_name)
    root = tree.getroot()
    name_candidates = []
    time = get_time_of_first_point(gpx_file_name)
    for metadata in root.findall(wrap_default_namespace('metadata')):
        for metadata_name in metadata.findall(wrap_default_namespace('name')):
            name_candidates.append(time + ' ' + metadata_name.text)
    for trk in root.findall(wrap_default_namespace('trk')):
        for track_name in trk.findall(wrap_default_namespace('name')):
            name_candidates.append(time + ' ' + track_name.text)

    converted_name_candidates = []
    min_length_index = -1
    min_length = 99999
    index = 0
    for name in name_candidates:
        new_name = ''.join(ch for ch in name if (ch.isalpha() or ch.isspace()))
        converted_name_candidates.append(new_name)
        cur_len = len(new_name)
        if cur_len < min_length:
            min_length = cur_len
            min_length_index = index
        index += 1

    try:
        target_name = name_candidates[min_length_index]
    except:
        target_name = "no_name" + str(utils.get_increment_integer())
    filtered_target_name = ''.join(ch for ch in target_name if (ch.isalnum() or ch in '., _-'))
    return filtered_target_name

    name_candidates.sort(key=len)
    return name_candidates[0]


def get_time_of_first_point(gpx_file_name):
    tree = ET.parse(gpx_file_name)
    root = tree.getroot()
    for trk in root.findall(wrap_default_namespace('trk')):
        for trkseg in trk.findall(wrap_default_namespace('trkseg')):
            for trkpt in trkseg.findall(wrap_default_namespace('trkpt')):
                for pt_time in trkpt.findall(wrap_default_namespace('time')):
                    return utils.get_pretty_time(pt_time.text)
