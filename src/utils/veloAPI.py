import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://api.jcdecaux.com/vls/v3/stations/'
params = {'contract': 'lyon', 'apiKey': os.environ.get('VELOV_API_KEY')}

print(os.environ.get('VELOV_API_KEY'))

stations = [
    {
        'name': 'mc do',
        'number': 10027
    },
    {
        'name': 'pharmacie',
        'number': 10079
    },
    {
        'name': 'en face',
        'number': 10011
    }
]


def get_velov_info():
    responses = []
    for station in stations:
        responses.append((requests.get(url + str(station['number']), params=params), station['name']))

    message = ""
    for response in responses:
        if response[0].ok:
            data = json.loads(response[0].content.decode('utf-8'))
            status = data['status']
            main_stands = data['mainStands']['availabilities']
            num_bikes = main_stands['bikes']
            num_stands = main_stands['stands']
            print(f"Le statut de la station {data['name']} ({response[1]}) est : {status}")
            print(f"Nombre de vélos disponibles: {num_bikes}")
            print(f"Nombre de bornes disponibles: {num_stands}")
            if status == 'OPEN':
                message += f"{response[1]}, {num_bikes}/{num_stands} vélos dispo\n"
        else:
            print("La requête a échoué")

    if message == "":
        return "Error"

    return message
