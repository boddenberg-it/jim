#!/usr/bin/python

from metrics_handler import evaluate_queues
from metrics_handler import evaluate_jobs

JENKINS_URL = 'https://jenkins.blobb.me'

evaluate_queues(JENKINS_URL)
#evaluate_jobs(JENKINS_URL, config)
