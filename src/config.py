import os


class Config:
    ATS_BASE_URL = os.getenv("ATS_BASE_URL", "https://mock-ats.local")
    ATS_API_KEY = os.getenv("ATS_API_KEY", "mock-api-key")
    ENV = os.getenv("ENV", "local")
