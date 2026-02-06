from src.services.ats_factory import get_ats_client
from src.utils.response import success_response, error_response


def handler(event, context):
    try:
        params = event.get("queryStringParameters") or {}

        page = int(params.get("page", 1))
        per_page = int(params.get("per_page", 2))

        client = get_ats_client()
        response = client.get_jobs(page=page, per_page=per_page)

        return success_response({
            "jobs": response["results"],
            "pagination": {
                "page": page,
                "per_page": per_page,
                "has_next": response["has_next"]
            }
        })

    except ValueError:
        return error_response("page and per_page must be integers", 400)

    except Exception as e:
        return error_response(str(e), 500)
