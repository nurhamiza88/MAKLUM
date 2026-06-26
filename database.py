import requests
from config import WEB_APP_URL


def save_feedback(data):

    try:

        response = requests.post(
            WEB_APP_URL,
            json=data,
            timeout=20
        )

        print("=" * 50)
        print("STATUS :", response.status_code)
        print("TEXT   :", response.text)
        print("=" * 50)

        return response.status_code == 200

    except Exception as e:

        print("=" * 50)
        print("ERROR :", e)
        print("=" * 50)

        return False