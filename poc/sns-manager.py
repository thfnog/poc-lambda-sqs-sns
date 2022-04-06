import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from aws_commons.snsClient import SNSClient
from random import *

sns = SNSClient()
SUBSCRIPTION_ARN = 'arn:aws:sns:us-east-1:123456789012:TEST_TOPIC'

def create_topic():
    """ SNS Client library for create topic. """
    try:
        print('Creating topic')
        topicArn = sns.create_topic('TEST_TOPIC')
        print('Topic created: %s' % topicArn)
    except Exception as e:
        print("Not possible to create topic: %s" % e)
        raise
    
    
def get_topics():
    try:
        print('Get all topics')
        topics = sns.list_topics()
        print(topics)
    except Exception as e:
        print("Not possible to send message: %s" % e)
        raise
    
    
def get_subscrition_topic():
    try:
        print('Get all topics')
        topics = sns.list_subscriptions_by_topic(SUBSCRIPTION_ARN)
        print(topics)
    except Exception as e:
        print("Not possible to send message: %s" % e)
        raise
    
    
def delete_topic():
    try:
        print('Get topic to delete')
        topic = sns.get_first_topic()
        print(topic)
        
        print('Deleting topic: %s' % topic)
        sns.delete_topic(topic_arn=topic)
    except Exception as e:
        print("Not possible to send message: %s" % e)
        raise
    
if __name__ == '__main__':
    globals()[sys.argv[1]]()
