get all jobs:

https://jenkins.blobb.me/view/all/api/json/?tree=jobs[_class,url]
iterate through each job and recursive for folder/mutliJob/matrixJob

#each job health stats:
#api/json/?pretty=true&tree=inQueue

each job queue stats:
api/json/?pretty=true&tree=builds[number] -> BUILD_PAINTING/2/api/json/?pretty=true&tree=duration,result,timestamp,builtOn
    -> additional stuff

checkstyle:
/4/checkstyleResult/api/json/?pretty=true&tree=numberOfWarnings,numberOfNormalPriorityWarnings,numberOfLowPriorityWarnings,numberOfHighPriorityWarnings,numberOfFixedWarnings
if nothing returned everything's fine.

shellcheck warnings/violations plugin stuff.
probably the same as gcc and checkstyle :D

gcc warnings:
&tree=numberOfWarnings,numberOfNormalPriorityWarnings,numberOfLowPriorityWarnings,numberOfHighPriorityWarnings,numberOfFixedWarnings,suites[cases[name]]
if nothing returned everything's fine.

JUnit ReportXML.
/45/testReport/api/json/?pretty=true&tree=failCount,passCount,skipCount,suites[cases[name]]
NOTE: add three values for totalCount.


evaluate folder (recursive), Pipeline, Matrix Project, FreeStyleProject, MultiJob
()
