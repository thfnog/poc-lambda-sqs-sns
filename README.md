# Python AWS SQS/SNS Example

Example Python App Consuming and Producing messages to AWS SQS/SNS

### Local Docker Environment
The example code relies on a running SQS service, the repo contains a Docker compose file that will spin up a configured SQS/SNS using Localstack.

* Install Docker Toolbox - [Instructions](https://www.docker.com/products/docker-toolbox)

* Run the docker environment `docker-compose up`

This will launch a SQS service listening on port `4575` for SNS and `4576` for SQS

### Build dependencies

* Python 3 `$ brew install python3`
* Virtual Env `$ sudo pip3 install virtualenv`

### Configure and Run

From the terminal enable & configure the application dependencies.
* `$ virtualenv env`
* `$ source env/bin/activate`
* `(env) (base) $ pip3 install -r requirements.txt`
* Serveless `(env) (base) $ npm install -g serverless@2`
* `(env) (base) $ serverless plugin install -n serverless-python-requirements`

Create SQS Queue and SNS Topic.
* `(env) (base) $ python poc/sqs-manager.py create_queue`
* `(env) (base) $ python poc/sns-manager.py create_topic`

You can now run the lambda.
* `(env) (base) $ sls invoke local -f <producer|consumer|publish|subscribe|unsubscribe> [options]`

SQS examples:
* `(env) (base) $ sls invoke local -f producer --path src/json/sqs-message.json`
* `(env) (base) $ sls invoke local -f consumer`

SNS examples:
* `(env) (base) $ sls invoke local -f subscribe --path src/json/sns-subscribe.json`
* `(env) (base) $ sls invoke local -f publish --path src/json/sns-publish.json`
* `(env) (base) $ sls invoke local -f unsubscribe --data 'eb06e413-ed5b-410e-bbce-b17b1da3f41c'`

To leave the virtual Environment.
* `(env) $ deactivate`
