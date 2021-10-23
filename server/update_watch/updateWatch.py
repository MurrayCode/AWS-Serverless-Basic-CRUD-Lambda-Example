import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('watches')

def lambda_handler(event, context):

    if ('body' not in event or
            event['httpMethod'] != 'PUT'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

    watch = json.loads(event['body'])
    watch_id = event['pathParameters']['id']
    params = {
        'id':watch_id
    }

    response = table.update_item(
        Key=params,
        #Note - name is reserved keyword update_item - had to use watchname
        UpdateExpression="set watchname = :n, brand = :b, price = :p",
        ExpressionAttributeValues={
            ':n': watch['name'],
            ':b': watch['brand'],
            ':p': watch['price']
        },
        ReturnValues="UPDATED_NEW"
    )
    print(response)
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({'msg': 'Activity updated'})
    }