# GPX Utils

These utilities provide easy way to work with raw gpx files. I create them because GUI applications to work with tracks sometimes remove useful information (for example, waypoints) from tracks.

## gpxclean

clean GPX track from noise information. Also can delete timestamps, elevation. Option `--merge_tracks` allows merge all tracks(there can be several tracks in one gpx file) to one track(`trk`, not into gpx file) with several segments.

```
usage: gpxclean.py [-h] [-o OUTPUT_DIR] [-t] [-e] [-d] [-r] [-w] [-m] [-n] [gpx_files [gpx_files ...]]

positional arguments:
  gpx_files

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
  -t, --ignore_time
  -e, --ignore_elevation
  -d, --ignore_metadata
  -r, --replace_original
  -w, --ignore_wpt
  -m, --merge_tracks
  -n, --auto_rename
```

## gpxmerge

merge several gpx files into one. 

```
usage: gpxmerge.py [-h] [-o OUTPUT_DIR] [-w] [-m] [gpx_files [gpx_files ...]]

positional arguments:
  gpx_files

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
  -w, --ignore_wpt
  -m, --merge_tracks
```

It can read list of files from stdin. So it can be combine with other tools with pipes:

```
find . -maxdepth 1 -type f -name "*.gpx" | gpxmerge
```

It was tested on Windows with Cygwin.

## gpxsplit

Split one GPX files to several. One track - one new file.	

```
usage: gpxsplit.py [-h] [-o OUTPUT_DIR] [gpx_files [gpx_files ...]]

positional arguments:
  gpx_files

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
```

## gpxextractname

Generate new file name from first point date and shortest metadata or track name.

```
usage: gpxextractname.py [-h] [-o OUTPUT_DIR] [-t] [gpx_files [gpx_files ...]]

positional arguments:
  gpx_files

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
  -t, --retrieve_time
```

## Examples

Find all tracks in current folder and merge them into one in default output folder (./output)

```
find . -maxdepth 1 -type f -name "*.gpx" | gpxmerge
```

Find all tracks in current folder and clean(*update name, pretty print, remove noise*) them with replacing:

```
find . -maxdepth 1 -type f -name "*.gpx" | gpxclean -r
```

## Prerequisites

python 3.8.1

## Develop

Next files uses from all scripts.

1. `gpxlib.py` - main logic.

2. `util.py` - helpers.

## Issues

- remove points with low speed.