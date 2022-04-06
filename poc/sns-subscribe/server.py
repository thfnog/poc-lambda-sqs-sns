import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aws_commons.snsClient import SNSClient
from random import *

def main():
    """ SNS Client library for subscribe to topics. """
    try:
        sns = SNSClient()
        
        print('Publish Message')
        body = {
            "protocol": "email",
            "endpoint": "test@sensedia.com"
        }
        sns.subscribe(message=body)
    except Exception as e:
        print("Not possible to send message: %s" % e)
        raise