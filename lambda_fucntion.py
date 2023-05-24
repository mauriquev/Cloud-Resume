import json
import boto3

def lambda_handler(event, context):

    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb')
    
    # Update visitor count
    response = dynamodb.update_item(
        TableName='WebsiteCount',
        Key={'id': {'S': 'count'}},
        UpdateExpression='ADD visitors :incr',
        ExpressionAttributeValues={':incr': {'N': '1'}},
        ReturnValues='UPDATED_NEW'
    )
    
    # Get the updated count
    count = response['Attributes']['visitors']['N']
    
    
    # Return the visitor count and enable CORS
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://www.mqresume.com',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
        'body': str(count)
    }
