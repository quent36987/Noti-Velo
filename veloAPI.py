import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://api.jcdecaux.com/vls/v3/stations/10027'
params = {'contract': 'lyon', 'apiKey': os.environ.get('VELOV_API_KEY')}

def get_velov_info():
    response = requests.get(url, params=params)

    if response.ok:
        data = json.loads(response.content.decode('utf-8'))
        status = data['status']
        main_stands = data['mainStands']['availabilities']
        num_bikes = main_stands['bikes']
        num_stands = main_stands['stands']
        print(f"Le statut de la station {data['name']} est : {status}")
        print(f"Nombre de vélos disponibles: {num_bikes}")
        print(f"Nombre de bornes disponibles: {num_stands}")
        return status, num_bikes, num_stands
    else:
        print("La requête a échoué")
        return None
