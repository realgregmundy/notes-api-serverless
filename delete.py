import os
import json
from uuid import uuid4
from datetime import datetime
from libs.dynamo_db import delete


def main(event, context):
    try:
        id = event['pathParameters']['id']
        user_id = event['requestContext']['identity']['cognitoIdentityId']
        key = {
            'userId': user_id,
            'noteId': id
        }
        if delete(os.getenv('tableName'), key):
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True
                },
                'body': json.dumps({
                    'message': f'Successfully delete item {id}.'
                })
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
