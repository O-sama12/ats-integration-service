import json
from src.services.ats_factory import get_ats_client
from src.utils.response import success_response, error_response
from src.utils.errors import ValidationError, ATSException


def handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        required_fields = ["name", "email", "job_id"]
        for field in required_fields:
            if field not in body:
                raise ValidationError(f"{field} is required")

        client = get_ats_client()
        candidate = client.create_candidate(body)
        application = client.attach_candidate_to_job(
            candidate["id"], body["job_id"]
        )

        return success_response({
            "candidate": candidate,
            "application": application
        }, status_code=201)

    except ValidationError as ve:
        return error_response(str(ve), 400)

    except ATSException as ae:
        return error_response(ae.message, ae.status_code)

    except Exception as e:
        return error_response(str(e), 500)

