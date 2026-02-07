import requests
from src.services.zoho_auth import get_access_token
from src.config import Config


class ZohoATSClient:
    def get_jobs(self, page=1, per_page=10):
        token = get_access_token()

        headers = {
            "Authorization": f"Zoho-oauthtoken {token}"
        }

        params = {
            "page": page,
            "per_page": per_page
        }

        # Zoho Recruit Job Openings API
        response = requests.get(
            f"{Config.ZOHO_API_BASE}/recruit/v2/Job_Openings",
            headers=headers,
            params=params
        )

        response.raise_for_status()
        data = response.json()

        records = data.get("data", [])

        jobs = []
        for record in records:
            jobs.append({
                "id": record.get("id"),
                "title": record.get("Job_Opening_Name"),
                "location": record.get("City"),
                "status": record.get("Job_Opening_Status"),
                "external_url": record.get("Career_Page_URL")
            })

        # Zoho provides pagination info under "info"
        info = data.get("info", {})
        has_next = info.get("more_records", False)

        return {
            "results": jobs,
            "has_next": has_next
        }
