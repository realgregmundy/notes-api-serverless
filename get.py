import os
import json
from uuid import uuid4
from datetime import datetime
from lib.dynamo_db import get


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
                'body': json.dumps(result)
            }
        else:
            raise Exception('Item not found!')
    except Exception as e:
        return {'statusCode': 500,
                'body': json.dumps(str(e))
                }
