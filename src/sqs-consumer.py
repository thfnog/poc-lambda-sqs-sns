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

    try:    
        
        response = SQS.receive_message(
            QueueUrl=QUEUE_URL,
            AttributeNames=[""],
            MaxNumberOfMessages=1,
            MessageAttributeNames=['All'],
            VisibilityTimeout=0,
            WaitTimeSeconds=10,
        )
        
        message = response['Messages'][0]
        
        logger.info('Deleting message after receive.')
        SQS.delete_message(
                QueueUrl=QUEUE_URL,
                ReceiptHandle=message['ReceiptHandle']
            )
    except Exception as e:
        logger.exception('Receive message from SQS queue failed!')
        message = str(e)
        status_code = 500

    return {'statusCode': status_code, 'body': json.dumps({'message': message})}