from src.services.ats_factory import get_ats_client
from src.utils.response import success_response, error_response


def handler(event, context):
    try:
        params = event.get("queryStringParameters") or {}
        job_id = params.get("job_id")

        if not job_id:
            return error_response("job_id query parameter is required", 400)

        client = get_ats_client()
        applications = client.get_applications(job_id)

        return success_response(applications)

    except Exception as e:
        return error_response(str(e), 500)
