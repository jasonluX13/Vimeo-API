from flask import Flask,request,url_for,redirect,render_template
import lib2to3
import json, urllib.request, urllib.error, urllib.parse #urllib.request, urllib.error
import hashlib

script=Flask(__name__)
@script.route("/")
def index():
    return "hello"
@script.route("/t/")
def tag():
    pubkey = "c6202d64bfb8be20e9a7986bda8963bc"
    privkey = "6b628dbfa98f15f39aa4cedc06f4b110650565e2"
    timestamp = "1"
    line = timestamp+pubkey+privkey
    hash = hashlib.md5()
    hash.update(line.encode('utf-8'))
    h = hash.hexdigest()
    #url="http://gateway.marvel.com/v1/comics/?ts=1&apikey=c6202d64bfb8be20e9a7986bda8963bc&hash=%s"
    url= "http://gateway.marvel.com/v1/public/characters?apikey=c6202d64bfb8be20e9a7986bda8963bc&hash=%s&ts=%s"
    url = url%(h,timestamp)
    print(url)
    request = urllib.request.urlopen(url)
    resultstring = request.read()
    result = json.loads(resultstring)
    s = ""
    print (result)
    for item in result['response']:
        print(item)
    try:
        s= s + "<img src=%s>"%(item['photos'][0]['original_size']['url'])
        print (s)
    except:
        pass
    return s
if __name__=="__main__":
    script.debug=True
    script.run(host="0.0.0.0",port=8000)