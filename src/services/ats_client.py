import uuid
from src.config import Config
from src.utils.errors import ATSException


class ATSClient:
    # class-level storage (persists across invocations in offline mode)
    candidates = {}
    applications = {}

    def __init__(self):
        self.base_url = Config.ATS_BASE_URL
        self.api_key = Config.ATS_API_KEY

    def get_jobs(self, page=1, per_page=2):
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

    # -------- Day 2 logic --------

    def create_candidate(self, candidate_data):
        if not candidate_data.get("email"):
            raise ATSException("Email is required", 400)

        candidate_id = str(uuid.uuid4())
        candidate = {
            "id": candidate_id,
            "name": candidate_data["name"],
            "email": candidate_data["email"],
            "phone": candidate_data.get("phone"),
            "resume_url": candidate_data.get("resume_url")
        }

        ATSClient.candidates[candidate_id] = candidate
        return candidate

    def attach_candidate_to_job(self, candidate_id, job_id):
        if not job_id:
            raise ATSException("Job ID is required", 400)

        application_id = str(uuid.uuid4())
        application = {
            "id": application_id,
            "candidate_id": candidate_id,
            "job_id": job_id,
            "status": "APPLIED"
        }

        ATSClient.applications[application_id] = application
        return application

    def get_applications(self, job_id):
        results = []

        for app in ATSClient.applications.values():
            if app["job_id"] == job_id:
                candidate = ATSClient.candidates.get(app["candidate_id"])
                if candidate:
                    results.append({
                        "id": app["id"],
                        "candidate_name": candidate["name"],
                        "email": candidate["email"],
                        "status": app["status"]
                    })

        return results
