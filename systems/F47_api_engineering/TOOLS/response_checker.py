def response_check(response: dict) -> dict:
    return {"has_status": "status" in response, "has_body": "body" in response}
