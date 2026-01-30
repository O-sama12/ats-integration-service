from src.services.ats_client import ATSClient
from src.utils.response import success_response, error_response


def handler(event, context):
    try:
        client = ATSClient()
        jobs = []

        page = 1
        while True:
            response = client.get_jobs(page=page)
            jobs.extend(response["results"])

            if not response["has_next"]:
                break
            page += 1

        return success_response(jobs)

    except Exception as e:
        return error_response(str(e), 500)
