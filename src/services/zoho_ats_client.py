import requests
from src.services.zoho_auth import get_access_token
from src.config import Config


class ZohoATSClient:
    def get_jobs(self, page=1, per_page=10):
        token = get_access_token()

        headers = {
            "Authorization": f"Bearer {token}"
        }

        # Zoho People does NOT support page/per_page
        response = requests.get(
            f"{Config.ZOHO_API_DOMAIN}/people/api/forms/employee/getRecords",
            headers=headers
        )

        response.raise_for_status()
        data = response.json()

        records = data.get("response", {}).get("result", [])

        jobs = []
        for idx, record in enumerate(records):
            jobs.append({
                "id": f"zoho-{idx}",
                "title": record.get("Employee_Name", "Employee"),
                "location": record.get("Location", "N/A"),
                "status": "OPEN",
                "external_url": None
            })

        return {
            "results": jobs,
            "has_next": False
        }
