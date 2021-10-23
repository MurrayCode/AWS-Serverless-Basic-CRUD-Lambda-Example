import boto3
from boto3.dynamodb.conditions import Key
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('watches')

def lambda_handler(message, context):
    if ('pathParameters' not in message or
            message['httpMethod'] != 'GET'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }
    watch_id = message['pathParameters']['id']

    response = table.query(
        KeyConditionExpression=Key('id').eq(watch_id)
    )
    print(response)
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }