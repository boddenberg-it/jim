#!/usb/bin/python3
import json
import requests
import pprint

def req(url):
    response = requests.get(url)
    return json.loads(response.text)


def jobs(jenkins_url):
    jobs = []
    json = req('%s/view/all/api/json/?tree=jobs[url]' % jenkins_url)
    for job in json['jobs']:
        # TODO: traverse folder
        jobs.append(job['url'])
    return jobs

def builds_of(job_url):
    # return ['https://jenkins.blobb.me/job/check_xml_report/45']
    builds = []
    json = req("%s/api/json/?pretty=true&tree=builds[number]" % job_url)
    try:
        for build in json['builds']:
            builds.append("%s%s" % (job_url, build['number']))
    except Exception:
        pass
    return builds

# init pretty-print
pp = pprint.PrettyPrinter(indent=4)

for job in jobs('https://jenkins.blobb.me/'):

    for build in (builds_of(job)):

        print build
        #?pretty&tree=duration,result,builtOn # builtOn only for none Pipeline jobs
        resp = req("%s/api/json/?tree=duration,result" % build)
        print("result: %s, duration %s" % (resp['result'],resp['duration']))

        # check whether compiler warnings,
        warnings = None
        resp = req("%s/api/json/?tree=actions[result[numberOfFixedWarnings,numberOfHighPriorityWarnings,numberOfLowPriorityWarnings,numberOfNewWarnings,numberOfNormalPriorityWarnings,numberOfWarnings]]" % build)
        for key in resp['actions']:
            try:
                warnings = key['result']
            except Exception:
                pass
        if warnings:
            # pp.pprint(warnings)
            print(warnings['numberOfFixedWarnings']) # etcetera pp

        xml_report = None
        resp = req("%s/api/json/?depth=3&tree=actions[failCount,skipCount,totalCount]" % build)
        try:
            for key in resp['actions']:
                if key['_class'] == 'hudson.tasks.junit.TestResultAction':
                    xml_report = key
        except Exception:
            pass
        if xml_report:
            # pp.pprint(key)
            print(xml_report['totalCount'])

        # TODO: check stuff for job e.g. matrix project, buildFlow, Pipeline (stages), Multijob etcetera pp
        # /api/json/?pretty&tree=runs[url]
        print
