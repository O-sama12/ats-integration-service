import requests
from src.config import Config

def get_access_token():
    response = requests.post(
        "https://accounts.zoho.in/oauth/v2/token",
        data={
            "grant_type": "refresh_token",
            "client_id": Config.ZOHO_CLIENT_ID,
            "client_secret": Config.ZOHO_CLIENT_SECRET,
            "refresh_token": Config.ZOHO_REFRESH_TOKEN,
        }
    )
    response.raise_for_status()
    return response.json()["access_token"]
