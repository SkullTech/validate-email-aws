import json

from validate import validate


def handler(event, context):
    query = event.get('queryStringParameters') or {}
    email = query.get('email')
    if not email:
        response = {
            'error': 'No email provided'
        }
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(response)
        }

    response = validate(email)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(response)
    }
