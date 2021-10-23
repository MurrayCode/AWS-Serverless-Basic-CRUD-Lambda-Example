import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('watches')

def lambda_handler(event, context):
    if ('body' not in event or
            event['httpMethod'] != 'POST'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }
    watch = json.loads(event['body'])

    params = {
        'id': str(uuid.uuid4()),
        'name': watch['name'],
        'brand': watch['brand'],
        'price': watch['price']
    }
    response = table.put_item(
        Item=params
    )
    print(response)

    return {
        'statusCode': 201,
        'headers':{},
        'body': json.dumps({'msg':'Watch Created'})
    }
