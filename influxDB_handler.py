#!/usb/bin/python3
import json
import requests

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
    builds = []
    json = req("%s/api/json/?pretty=true&tree=builds[number]" % job_url)
    try:
        for build in json['builds']:
            builds.append("%s%s" % (job_url, build['number']))
    except Exception:
        pass
    return builds

for job in jobs('https://jenkins.blobb.me/'):

    for build in (builds_of(job)):
        print build
        #?pretty&tree=duration,result,builtOn # builtOn only for none Pipeline jobs
        resp = req("%s/api/json/?tree=duration,result" % build)
        print("result: %s, duration %s" % (resp['result'],resp['duration']))

    # check whether compiler warnings,
        resp = req("%s/api/json/?depth=3&tree=actions[result[numberOfFixedWarnings,numberOfHighPriorityWarnings,numberOfLowPriorityWarnings,numberOfNewWarnings,numberOfNormalPriorityWarnings,numberOfWarnings]]" % build)
        try:
            print(resp['result[numberOfFixedWarnings]'])
            print('found!')
        except Exception:
            pass

    #  check for xml unit report
    #/api/json/?pretty&tree=actions[failCount,skipCount,totalCount]
        resp = req("%s/api/json/?depth=3&tree=actions[failCount,skipCount,totalCount]" % build)
        try:
            print(resp['totalCount'])
        except Exception:
            pass

    # matrix project
    # /api/json/?pretty&tree=runs[url]
        print
#import urllib.request
#r = urllib.request.urlopen('https://jenkins.blobb.me/view/all/api/json/?tree=jobs[url]')
#print(r.read())
