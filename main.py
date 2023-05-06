import url_map
from flask import Flask, request, abort

app = Flask(__name__)

@app.post("/map")
def map():
    url = request.form.get("url")

    return url_map.mapUrl(url)

@app.get("/map/<hash>")
def getUrlbyHash(hash):
    url = url_map.getUrlByHash(hash)
    if not url:
        abort(404)
    return url_map.getUrlByHash(hash)
    

if __name__ == "__main__":
    app.run()