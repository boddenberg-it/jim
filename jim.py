#!/usr/bin/python

# jenkins dependency (pip install jenkinsapi)
import jenkinsapi
import pprint

from jenkinsapi.jenkins import Jenkins
from metrics_handler import obtain_build_information

JENKINS_URL = 'https://jenkins.blobb.me'
pp = pprint.PrettyPrinter(indent=4)

def evaluate_queues(jobs):
    for job in jobs:
        if jenkins[job].is_queued():
            print("%s is queueing") % job
        else:
            print "not queueing B)"

def evaluate_jobs(jobs):
    for job in jobs:
        try:
            oldest = jenkins[job].get_first_build().get_number()
            latest = jenkins[job].get_last_completed_build().get_number()

            # TODO: think about not always resending same value
            current = oldest

            while(current < latest):
                try:
                    runs = jenkins[job].get_matrix_runs()
                    for run in runs:
                        print "Evaluating matrix run %s" % run
                        obtain_build_information(jenkins[run])
                except Exception:
                    obtain_build_information(jenkins[job][current])
                current += 1

        except Exception:
            print "'%s' did not run yet, skipping" % job

# init jenkinsapi
print " "
print "Initialising jenkinsapi object..."
jenkins = Jenkins(JENKINS_URL)
# load jobs
print " "
print "Obtaining jobs..."
jobs = jenkins.keys()
print " "
print "All found jobs:"
pp.pprint(jobs)
print " "

evaluate_queues(jobs)
# evaluate_jobs(jobs)
