import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

class SNSClient:
    """ An abstraction over the AWS SNS api, allowing for simple consumption of SNS """

    def __init__(self, endpoint_url='http://localhost:4575', region='us-east-1'):

        # Initialise Boto3 Session
        session = boto3.session.Session()

        # Initialise SNS client
        self.sns = session.client(
            'sns',
            region_name=region,
            endpoint_url=endpoint_url,
            aws_access_key_id='ACCESS_KEY',
            aws_secret_access_key='SECRET_KEY',
            aws_session_token='SESSION_TOKEN',
        )
        print("SNSClient Initialised")

    def create_topic(self, name):
        """ Create Topic in SNS, returning the TopicArn """
        response = self.sns.create_topic(
            Name=name
        )
        print("TopicCreated -> %s" % response)
        topicArn = response['TopicArn']
        return topicArn
    
    def list_topics(self):
        """
        Lists topics for the current account.
        :return: An iterator that yields the topics.
        """
        try:
            topics_iter = self.sns.list_topics()
            logger.info("Got topics.")
        except ClientError:
            logger.exception("Couldn't get topics.")
            raise
        else:
            return topics_iter
        
    def get_first_topic(self):
        try:
            topics_iter = self.sns.list_topics()
            topicArn = topics_iter['Topics'][0]['TopicArn']
            logger.info("Got topics.")
        except ClientError:
            logger.exception("Couldn't get topics.")
            raise
        else:
            return topicArn
        
    def list_subscriptions(self, topic=None):
        """
        Lists subscriptions for the current account, optionally limited to a
        specific topic.
        :param topic: When specified, only subscriptions to this topic are returned.
        :return: An iterator that yields the subscriptions.
        """
        try:
            if topic is None:
                subs_iter = self.sns.subscriptions.all()
            else:
                subs_iter = topic.subscriptions.all()
            logger.info("Got subscriptions.")
        except ClientError:
            logger.exception("Couldn't get subscriptions.")
            raise
        else:
            return subs_iter
    
    def delete_topic(self, topic_arn):
        """ Delete the topic, given the following URL """
        self.sns.delete_topic(
            TopicArn=topic_arn
        )

    def subscribe(self, topic, protocol):
        """ Subscribe to the specified SNS topic """
        response = self.sns.subscribe(
            TopicArn=topic,
            Protocol=protocol,
        )
        subscriptionArn = response['SubscriptionArn']
        print("SubscriptionArn -> %s" % subscriptionArn)
        return subscriptionArn
    
    def unsubscribe(self, subscriptionArn):
        """ Unsubscribe to the specified SNS topic """
        self.sns.unsubscribe(
            SubscriptionArn=subscriptionArn
        )
        
    def list_subscriptions_by_topic(self, topic):
        """ List of subscribe to the specified SNS topic """
        return self.sns.list_subscriptions_by_topic(
            TopicArn=topic
        )

    def publish(self, **kwargs):
        """ Receive Message from Queue """
        response = self.sns.publish(
            TopicArn=kwargs['topicArn'],
            PhoneNumber=kwargs['phoneNumber'],
            TargetArn=kwargs['targetArn'],
            Message=kwargs['message'],
            Subject=kwargs['subject'],
            MessageStructure=kwargs['messageStructure']
        )        
        message = response['MessageId']
        print("MessageId -> %s" % message)
        return message
