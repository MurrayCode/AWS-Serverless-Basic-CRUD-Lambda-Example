import boto3
from boto3.dynamodb.conditions import Key
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('watches')

def lambda_handler(event, context):
    if ('pathParameters' not in event or
            event['httpMethod'] != 'GET'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }
    watch_id = event['pathParameters']['id']

    response = table.query(
        KeyConditionExpression=Key('id').eq(watch_id)
    )
    print(response)
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }