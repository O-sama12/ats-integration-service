import time
import requests
from src.config import Config

_access_token = None
_token_expiry = 0


def get_access_token():
    global _access_token, _token_expiry

    # Reuse token if still valid
    if _access_token and time.time() < _token_expiry:
        return _access_token

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
    data = response.json()

    _access_token = data["access_token"]
    _token_expiry = time.time() + data.get("expires_in", 3600) - 60

    return _access_token
