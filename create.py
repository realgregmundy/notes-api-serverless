import os
import json
from uuid import uuid4
from datetime import datetime
from lib.dynamo_db import put


def main(event, context):
    try:
        data = json.loads(event['body'])
        item = {
            'userId': '123',
            'noteId': str(uuid4()),
            'content': data['content'],
            'attachment': data['attachment'],
            'createdAt': str(datetime.utcnow())
        }
        if put(os.getenv('tableName'), item):
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            raise Exception('Invalid message body.')
    except Exception as e:
        return {'statusCode': 500,
                'body': json.dumps(str(e))
                }
