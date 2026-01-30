from src.config import Config


class ATSClient:
    def __init__(self):
        self.base_url = Config.ATS_BASE_URL
        self.api_key = Config.ATS_API_KEY

    def get_jobs(self, page=1, per_page=2):
        # Mock ATS response
        jobs = [
            {
                "id": "job-1",
                "title": "Backend Engineer",
                "location": "Remote",
                "status": "OPEN",
                "external_url": "https://company.com/jobs/1"
            },
            {
                "id": "job-2",
                "title": "Data Engineer",
                "location": "Bangalore",
                "status": "OPEN",
                "external_url": "https://company.com/jobs/2"
            },
            {
                "id": "job-3",
                "title": "ML Engineer",
                "location": "Hyderabad",
                "status": "CLOSED",
                "external_url": "https://company.com/jobs/3"
            }
        ]

        start = (page - 1) * per_page
        end = start + per_page

        return {
            "results": jobs[start:end],
            "has_next": end < len(jobs)
        }
