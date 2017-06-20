#!/usb/bin/python

# jenkins dependency (pip install jenkinsapi)
import jenkinsapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

from jenkinsapi.jenkins import Jenkins

jenkins = ""

def log(msg):
    print " "
    print "msg"

# already filter jobs, to only hold filtered ones!
def load_jobs(url):
    log("Initialising jenkinsapi object...")
    jenkins = Jenkins(JENKINS_URL)
    log("Obtaining jobs...")
    jobs = jenkins.keys()
    log("All found jobs:")
    pp.pprint(jobs)

    jenkins_server = collections.namedtuple('Jenkins', ['jenkins', 'jobs'])
    return jenkins_server

def evaluate_queues(url):
    jenkins = load_jobs()
    jobs = jenkins.jobs
    jenkins = jenkins.jenkins

    for job in jobs:
        if jenkins[job].is_queued():
            print("%s is queueing") % job
        else:
            print "not queueing B)"

def evaluate_jobs(jenkins, jobs):
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

def obtain_build_information(job):
    print "Evaluating '%s'" % job
    try:
        # TODO: check whether format is influx conform
        number = job.get_number()
        print number
        print job.get_timestamp()
        print job.get_duration()
        print job.get_status()
    except ValueError:
        print "'%s' did not run yet, skipping." % job
    try:
        print job.get_slave()
    except Exception:
        print "%s does not provide any slave information" % (job)
    #print job.get_upstream_job_name()
    #print job.get_params()
    try:
        print job.get_revision()
    except Exception:
        print "%s does not provide any revision" % (job)
    print " "

def obtain_lint_information():
    print "tbc..."

def obtain_test_information():
    print "tbc..."