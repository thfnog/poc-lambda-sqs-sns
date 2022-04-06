import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aws_commons.sqsClient import SQSClient
from random import *

queue_url = 'TEST_QUEUE'

def main():
    """ SQS Client library for consume messages. """
    try:
        sqs = SQSClient()
        
        print('Consume Messages')
        msg = sqs.consume_next_message(queue_url)
        
        msg_id = msg['MessageId']
        print("Message ID -> %s" % msg_id)

        print('Delete Message')
        sqs.delete_message(queue_url, msg['ReceiptHandle'])
    except Exception as e:
        print("Not possible to consume messages: %s" % e)
        raise
