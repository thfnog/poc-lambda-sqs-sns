import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aws_commons.sqsClient import SQSClient
from random import *

sqs = SQSClient()
SQS_QUEUE = 'TEST_QUEUE'

def create_queue():
    """ SQS Client library for create queue. """
    try:
        print('Creating queue')
        queue_url = sqs.create_queue(SQS_QUEUE)
        print('Queue created: %s' % queue_url)
    except Exception as e:
        print("Not possible to create queue: %s" % e)
        raise
    
if __name__ == '__main__':
    globals()[sys.argv[1]]()
