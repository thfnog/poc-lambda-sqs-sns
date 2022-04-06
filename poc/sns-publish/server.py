import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aws_commons.snsClient import SNSClient
from random import *

def main():
    """ SNS Client library for produce messages. """
    try:
        sns = SNSClient()
        
        print('Publish Message')
        body = 'Some Awesome message {0}'.format(randint(1, 1000))
        sns.publish(message=body)
    except Exception as e:
        print("Not possible to send message: %s" % e)
        raise