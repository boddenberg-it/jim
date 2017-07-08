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
    metrics_of(builds_of(job)))


#import urllib.request
#r = urllib.request.urlopen('https://jenkins.blobb.me/view/all/api/json/?tree=jobs[url]')
#print(r.read())
