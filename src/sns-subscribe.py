import json
import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ENDPOINT_URL = os.getenv('SNS_ENDPOINT_URL') 
SNS_TOPIC = os.getenv('SNS_TOPIC')
SNS = boto3.client('sns', endpoint_url=ENDPOINT_URL)


def handler(event, context):
    status_code = 200
    message = ''

    try:

        response = SNS.subscribe(
            TopicArn=SNS_TOPIC,
            Protocol=event['protocol'],
            Endpoint=event['endpoint'],
            ReturnSubscriptionArn=True
        )

        message = 'Subscribe to topic accepted! SubscriptionArn: ' + response['SubscriptionArn']
    except Exception as e:
        logger.exception('Subscribe to SNS topic failed!')
        message = str(e)
        status_code = 500

    return {'statusCode': status_code, 'body': json.dumps({'message': message})}