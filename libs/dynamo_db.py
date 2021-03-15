import boto3

DYNAMO_DB = boto3.resource('dynamodb')


def get(table_name: str, key: dict = None):
    try:
        table = DYNAMO_DB.Table(table_name)
        if key:
            result = table.get_item(Key=key)
            return result['Item']
        else:
            pass
    except Exception:
        return None


def put(table_name: str, item: dict) -> bool:
    try:
        table = DYNAMO_DB.Table(table_name)
        table.put_item(Item=item)
        return True
    except Exception:
        return False


def query(table_name: str, key_condition_expression,
          expression_attribute_values: dict):
    try:
        table = DYNAMO_DB.Table(table_name)
        result = table.query(
            KeyConditionExpression=key_condition_expression,
            ExpressionAttributeValues=expression_attribute_values)
        return result['Items']
    except Exception as e:
        print(str(e))
        return None


def update(table_name: str, key: dict, update_expression: str,
           expression_attribute_values: dict):
    try:
        table = DYNAMO_DB.Table(table_name)
        result = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues='ALL_NEW')
        return result['Attributes']
    except Exception as e:
        print(str(e))
        return None


def delete(**kwargs):
    pass
