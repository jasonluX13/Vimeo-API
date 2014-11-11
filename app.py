from flask import Flask, request, url_for, redirect, render_template
import json, urllib.request, urllib.error, urllib.parse
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/t/",methods=["GET","POST"])
@app.route("/t/<tag>",methods=["GET","POST"])
def tag(tag=""):
    if request.method == "GET":
        return render_template("index.html")
    else:
        tag = request.form["channel"]
        try:
            url="http://vimeo.com/api/v2/channel/%s/videos.json"
            url = url%(tag)
            request = urllib.request.urlopen(url)
            resultstring = request.read()
            result = json.loads(resultstring.decode('utf-8'))
            titles = []
            url = []
            thumbnails = []
            i = 0
            #print(len(result))
            while i < len(result):
                titles.append( result[i]["title"])
                url.append(result[i]["url"])
                thumbnails.append(result[i]["thumbnail_medium"])
                i=i+1
            print (titles)
            return render_template("search.html",
                                    titles = titles,
                                    url = url,
                                    thumbnails = thumbnails,
                                    all = result) 
        except (urllib.error.URLError):
            return('Sorry, that is not a valid channel.')
        
if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)