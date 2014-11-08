from flask import Flask,request,url_for,redirect,render_template
import json, urllib.request, urllib.error, urllib.parse
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/t/<tag>")
def tag(tag=""):
    try:
        url="http://vimeo.com/api/v2/channel/%s/videos.json"
        url = url%(tag)
        request = urllib.request.urlopen(url)
        resultstring = request.read()
        result = json.loads(resultstring.decode('utf-8'))
        #print(resultstring)
    
        
        return resultstring
    except (urllib.error.URLError):
        return('Sorry, that is not a valid channel.')
        
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)