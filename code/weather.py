import urllib2
import json
import re

def weather():
    url="http://api.wunderground.com/api/a0a3b1a2fcc7d9e0/hourly/q/NY/New_York.json"
    wsign = 0
    data=urllib2.urlopen(url)
    Data=data.read()
    #Data= Data.split('\n', 1)[1]
    for i in range(12):
        res = json.loads(Data)['hourly_forecast'][i]['condition']
        print res
	if re.search('rain',res) or re.search('Rain',res):
	    return rain
    condition = json.loads(Data)['hourly_forecast'][0]['condition']
    return condition.lower()