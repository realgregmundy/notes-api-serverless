import os
import json
from uuid import uuid4
from datetime import datetime
from libs.dynamo_db import get


def main(event, context):
    try:
        id = event['pathParameters']['id']
        user_id = event['requestContext']['identity']['cognitoIdentityId']
        key = {
            'userId': user_id,
            'noteId': id
        }
        result = get(os.getenv('tableName'), key)
        if result:
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True
                },
                'body': json.dumps(result)
            }
        else:
            raise Exception('Item not found!')
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps(str(e))
        }
