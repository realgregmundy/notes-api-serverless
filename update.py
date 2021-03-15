import os
import json
from uuid import uuid4
from datetime import datetime
from libs.dynamo_db import update


def main(event, context):
    try:
        data = json.loads(event['body'])
        user_id = '123'
        id = event['pathParameters']['id']
        # user_id = event['requestContext']['identity']['cognitoIdentityId']

        key = {
            'userId': user_id,
            'noteId': id
        }
        update_expression = 'SET content = :content, attachment = :attachment'
        expression_attribute_values = {
            ':attachment': data['attachment'] if data['attachment'] else None,
            ':content': data['content'] if data['content'] else None
        }
        result = update(os.getenv('tableName'), key, update_expression,
                        expression_attribute_values)
        if result:
            return {
                'statusCode': 200,
                'body': json.dumps(result)
            }
        else:
            raise Exception(f'Cannot find item with id {id}.')
    except Exception as e:
        return {'statusCode': 500,
                'body': json.dumps(str(e))
                }
