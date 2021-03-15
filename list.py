import os
import json
from uuid import uuid4
from datetime import datetime
from lib.dynamo_db import query


def main(event, context):
    try:
        key_condition_expression = 'userId = :userId'
        expression_attribute_values = {
            ':userId': '123'
        }
        result = query(os.getenv('tableName'),
                       key_condition_expression, expression_attribute_values)
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