import requests
from config import WEB_APP_URL


def save_feedback(data):

    try:

        response = requests.post(

            WEB_APP_URL,

            json=data,

            timeout=20

        )

        return response.status_code == 200

    except Exception:

        return False