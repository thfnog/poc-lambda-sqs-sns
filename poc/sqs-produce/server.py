import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aws_commons.sqsClient import SQSClient
from random import *

queue_url = 'TEST_QUEUE'

def main():
    """ SQS Client library for produce messages. """
    try:
        sqs = SQSClient()
        
        print('Send Message')
        body = 'Some Awesome message {0}'.format(randint(1, 1000))
        sqs.send_message(queue_url, body)
    except Exception as e:
        print("Not possible to send message: %s" % e)
        raise
