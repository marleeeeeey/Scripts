# GPX Utils

These utilities provide easy way to work with raw gpx files. I create them because GUI applications to work with tracks sometimes remove useful information (for example, waypoints) from tracks.

1. `gpxcleaner` - to clean GPX track from noise information. Also can delete timestamps, elevation. Option `--merge_tracks` allows merge all tracks(there can be several tracks in one gpx file) to one track(`trk`, not into gpx file) with several segments.
2. `gpxmerge` - merge several gpx files into one.

## Usage

```
usage: gpxcleaner.py [-h] [-i INPUT_GLOB_MASK] [--ignore_time] [--ignore_elevation] [--ignore_metadata]
                     [--replace_original] [--merge_tracks] [-o OUTPUT_DIR]

usage: gpxmerge.py [-h] [-i INPUT_GLOB_MASK] [-o OUTPUT_DIR] [--merge_tracks]
```

## Examples

```
python gpxcleaner.py -i"C:\**\*.gpx"
python gpxcleaner.py -iFile.gpx --ignore_time --ignore_elevation
python gpxmerge.py -iC:\raw\*.gpx --merge_tracks
```



## Prerequisites

python 3.8.1

## Issues

- remove points with low speed.