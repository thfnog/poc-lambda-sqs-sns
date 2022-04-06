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

    if not event.get('message'):
        return {'statusCode': 400, 'body': json.dumps({'message': 'No message was found'})}

    try:

        SNS.publish(
            TopicArn=SNS_TOPIC,
            PhoneNumber=event['phoneNumber'],
            TargetArn=event['targetArn'],
            Message=event['message'],
            Subject=event['subject'],
            MessageStructure=event['messageStructure']
        )

        message = 'Publish to topic accepted!'
    except Exception as e:
        logger.exception('Publish message to SNS topic failed!')
        message = str(e)
        status_code = 500

    return {'statusCode': status_code, 'body': json.dumps({'message': message})}