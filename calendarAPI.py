import requests
from icalendar import Calendar
from datetime import datetime, date, timedelta
import pytz

url = 'https://zeus.ionis-it.com/api/group/541/ics/m2VIjow6S9'

# Télécharge le fichier ICS depuis l'URL donnée
response = requests.get(url)

if response.ok:
    # Parse le fichier ICS en un objet Calendar
    cal = Calendar.from_ical(response.text)

    # Récupère les informations d'événement requises pour la journée d'aujourd'hui
    today = date.today() + timedelta(days=1)
    events = []
    for event in cal.walk('VEVENT'):
        start = event.get('dtstart').dt
        if start.date() == today:
            name = event.get('summary')
            events.append({'name': name, 'start': start})

    # Trouve le premier événement de la journée d'aujourd'hui
    first_event = None
    if len(events) > 0:
        events.sort(key=lambda e: e['start'])
        first_event = events[0]

    # Affiche le premier événement de la journée d'aujourd'hui, s'il existe
    if first_event is not None:
        tz = pytz.timezone('Europe/Paris')
        local_start = first_event['start'].astimezone(tz)
        print(f'Premier événement de la journée : {first_event["name"]} à {local_start.strftime("%H:%M")}')
    else:
        print('Aucun événement prévu pour la journée d\'aujourd\'hui')
else:
    print('Impossible de télécharger le fichier ICS')
