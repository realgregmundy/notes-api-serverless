import os
import json
from uuid import uuid4
from datetime import datetime
from libs.dynamo_db import put


def main(event, context):
    try:
        data = json.loads(event['body'])
        user_id = event['requestContext']['identity']['cognitoIdentityId']
        item = {
            'userId': user_id,
            'noteId': str(uuid4()),
            'content': data['content'],
            'attachment': data['attachment'],
            'createdAt': str(datetime.utcnow())
        }
        if put(os.getenv('tableName'), item):
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True
                },
                'body': json.dumps(item)
            }
        else:
            raise Exception('Invalid message body.')
    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps(str(e))
        }
