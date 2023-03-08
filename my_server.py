from datetime import datetime
import schedule
import time
import calendarAPI
import veloAPI
import notifAPI
import pytz


# like HH:MM
def format_time(date):
    return date.strftime('%H:%M')


def job():
    print("I'm working...")
    name, start = calendarAPI.get_first_event_today()

    # if there is no event today, return
    if name is None:
        return

    # if the event is already over, return
    tz = pytz.timezone('Europe/Paris')
    now = datetime.now().astimezone(tz)

    if start < now:
        print(f" event {name} is already over")
        return

    # calculate the time left before the event
    time_left = start - now
    print(f' time left: {time_left} before the event {name}')

    # transform the time left into seconds
    time_left_seconds = time_left.total_seconds()
    print(f' time left in seconds: {time_left_seconds}')

    # wait 30 minutes before the event
    time.sleep(time_left_seconds - 1800)

    # send the notification
    status, num_bikes, num_stands = veloAPI.get_velov_info()
    print(f' status: {status}, num_bikes: {num_bikes}, num_stands: {num_stands}')

    if status == 'OPEN':
        notifAPI.send_notification('VELO',
                                   f'il y a {num_bikes} vélos et {num_stands} places, {name} commence a {format_time(start)}')


# every day at 7:00AM without the weekends
schedule.every().day.at("07:00").do(job)

if __name__ == "__main__":
    print("loading")
    while True:
        schedule.run_pending()
        time.sleep(1)
