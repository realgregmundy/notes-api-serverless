import os
import json
from uuid import uuid4
from datetime import datetime
from libs.dynamo_db import query


def main(event, context):
    try:
        user_id = event['requestContext']['identity']['cognitoIdentityId']
        key_condition_expression = 'userId = :userId'
        expression_attribute_values = {
            ':userId': user_id
        }
        result = query(os.getenv('tableName'),
                       key_condition_expression, expression_attribute_values)
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
