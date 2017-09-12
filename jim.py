#!/usr/bin/python
from metrics_handler import init_jenkins
from metrics_handler import evaluate_queues
from metrics_handler import evaluate_jobs

#from influxdb_handler import init_influxdb
#from influxdb_handler import send_metrics

init_jenkins('https://jenkins.blobb.me')
#init_influxdb('','','')

# works, but only prints which job is queueing not assigned label(!)
#evaluate_queues()

#
evaluate_jobs()
