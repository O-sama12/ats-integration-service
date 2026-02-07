from src.config import Config
from src.services.zoho_recruit_ats_client import ZohoATSClient
from src.services.ats_client import ATSClient as MockATSClient


def get_ats_client():
    if Config.ATS_PROVIDER == "zoho":
        return ZohoATSClient()
    return MockATSClient()
