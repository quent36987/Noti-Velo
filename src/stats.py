from datetime import datetime
import schedule
import time
from utils import veloAPI
import pytz

tz = pytz.timezone('Europe/Paris')


def format_time(date):
    return date.strftime('%H:%M')


stations = [10027, 10079, 10011]


def job():
    # create line like : date,station id,status,available bikes,available stands
    # 2020-10-01 07:00:00,10027,OPEN,2,18

    date = datetime.now().astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')

    for station in stations:
        status, available_bikes, available_stands = veloAPI.get_station_info(station)
        line = f'{date},{station},{status},{available_bikes},{available_stands}'

        print(line)

        with open('data/data.csv', 'a') as f:
            f.write(line + ' \n')


print("starting !", datetime.now(), datetime.now().astimezone(tz))
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
