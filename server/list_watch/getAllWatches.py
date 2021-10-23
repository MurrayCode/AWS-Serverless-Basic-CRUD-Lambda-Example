import boto3
import os
import json


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('watches')


def lambda_handler(event, context):
    if ('httpMethod' not in event or
            event['httpMethod'] != 'GET'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }
    
    response = table.scan()
    print(response)

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }