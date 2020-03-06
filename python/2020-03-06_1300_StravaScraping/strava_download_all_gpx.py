from stravabot import StravaBot
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", type=str, required=True, help = "email for authentication")
    parser.add_argument("-p", "--password", type=str, required=True)
    parser.add_argument("-s", "--skip", default=0, type=int, help = 'Skip elements from begin')
    args = parser.parse_args()

    try:
        bot = StravaBot()
        bot.login(args.username, args.password)
        bot.download_tracks(args.skip)
        print('Downloading complete')
    except Exception as e:
        print('Error: application closed with error:', str(e))
    finally:
        bot.close_browser()
main()