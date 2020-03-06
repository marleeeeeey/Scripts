from stravabot import StravaBot
from secrets import username, password

def main():
    bot = StravaBot()
    bot.login(username, password)
    bot.download_tracks(665)
    print('Downloading complete')

main()