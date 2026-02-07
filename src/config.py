import os


class Config:
    # Environment
    ENV = os.getenv("ENV", "local")

    # ATS provider switch
    ATS_PROVIDER = os.getenv("ATS_PROVIDER", "mock")

    # Mock ATS
    ATS_BASE_URL = os.getenv("ATS_BASE_URL")
    ATS_API_KEY = os.getenv("ATS_API_KEY")

    # Zoho Recruit OAuth
    ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
    ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
    ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")

    # Zoho Recruit API base (India DC)
    ZOHO_API_BASE = os.getenv("ZOHO_API_BASE", "https://www.zohoapis.in")
