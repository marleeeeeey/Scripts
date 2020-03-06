# Strava Utils

Script for downloading all tracks from Strava.

## Prerequisites

1. [chromedriver](https://chromedriver.chromium.org/)
   1. windows - unzip and add directory to path
   2. linux, macos - unzip, move to `/usr/local/bin`
2. `pip install selenium`

## Usage

```
usage: strava_download_all_gpx.py [-h] -u USERNAME -p PASSWORD [-s SKIP]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        email for authentication
  -p PASSWORD, --password PASSWORD
  -s SKIP, --skip SKIP  Skip elements from begin
```

## Developing

1. `python -i stravabot.py` - use this command to make StravaBot class available for experiments in python console.

2. see example in `strart_stravabot.py`. Create a `secrets.py` file with variables:

```
 username = 'your_username'
 password = 'your_password'
```
