from flask import Flask,request,url_for,redirect,render_template
import json, urllib2
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/t/<tag>")
def tag(tag=""):
    try:
        url="http://vimeo.com/api/v2/channel/%s/videos.json"
        url = url%(tag)
        request = urllib2.urlopen(url)
        resultstring = request.read()
        result = json.loads(resultstring)
        
        titles = []
        url = []
        thumbnails = []
        i = 0
        while i < len(result):
            titles.append( result[i]["title"])
            url.append(result[i]["url"])
            thumbnails.append(result[i]["thumbnail_medium"])
            i=i+1
        print (titles)
        return render_template("search.html",
                                titles = titles,
                                url = url,
                                thumbnails = thumbnails) 
    
    except (urllib2.URLError):
        return('Sorry, that is not a valid channel.')
        
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)
