from flask import Flask,request,url_for,redirect,render_template
import json, urllib2
app=Flask(__name__)
@app.route("/")
def index():
    return "hello"
    
@app.route("/t/<tag>")
def tag(tag=""):
    try:
        url="http://vimeo.com/api/v2/channel/%s/videos.json"
        url = url%(tag)
        request = urllib2.urlopen(url)
        resultstring = request.read()
        return resultstring
    except (urllib2.URLError):
        return('Sorry, that is not a valid channel.')
        
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)