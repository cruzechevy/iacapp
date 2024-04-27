import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyDynamoDBTable')

def post_handler(event, context):
    body = json.loads(event['body'])
    id = body['id']
    name = body['name']

    table.put_item(
        Item={
            'id': id,
            'Name': name
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully!')
    }