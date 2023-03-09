import pushbullet
import os
from dotenv import load_dotenv

load_dotenv()

# Remplacez YOUR_API_KEY par votre propre token d'authentification Pushbullet
api_key = os.environ.get('PUSHBULLET_API_KEY')
pb = pushbullet.Pushbullet(api_key)


def send_notification(title, body):
    pb.push_note(title, body)
