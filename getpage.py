import urllib2
import json


url="""
http://gateway.marvel.com/v1/comics/?ts=1&apikey=c6202d64bfb8be20e9a7986bda8963bc&hash=fe624c998b67c8998326e513e73a34da
"""
request = urllib2.urlopen(url)
result = request.read()
d = json.loads(result)
rlist = d['responseData']['results']
for r in rlist:
	print r['titleNoFormatting']
	print r['url']

'''
Request Url: http://gateway.marvel.com/v1/public/comics
Request Method: GET
Params: {   "apikey": "your api key",
            "ts": "a timestamp",
            "hash": "your hash" }
Headers:{
    Accept: */*
}
'''
