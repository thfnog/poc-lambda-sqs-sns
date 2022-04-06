import json
import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

QUEUE_URL = os.getenv('SQS_QUEUE_URL')
ENDPOINT_URL = os.getenv('SQS_ENDPOINT_URL') 
SQS = boto3.client('sqs', endpoint_url=ENDPOINT_URL)


def handler(event, context):
    status_code = 200
    message = ''

    if not event.get('body'):
        return {'statusCode': 400, 'body': json.dumps({'message': 'No body was found'})}

    try:
        message_attrs = {
            'AttributeName': {'StringValue': 'AttributeValue', 'DataType': 'String'}
        }
                
        SQS.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(event['body']),
            MessageAttributes=message_attrs
        )
        
        message = 'Message accepted!'
    except Exception as e:
        logger.exception('Sending message to SQS queue failed!')
        message = str(e)
        status_code = 500

    return {'statusCode': status_code, 'body': json.dumps({'message': message})}