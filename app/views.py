from flask import render_template
from . import app
from urllib import request,parse
import json

@app.route('/')
def home():
    params={
    "api_key":"rJM3VmADEJHGZR2wo6gnANb9TzYVhX5c",
    "limit":"10",
    "q":"moneyheist"
    }
    qrstring=parse.urlencode(params)
    base_url='https://api.giphy.com/v1/gifs/search?'
    req=request.urlopen(base_url+qrstring)
    resp=req.read()
    apires=json.loads(resp)
    data=apires["data"]
   

    return render_template('index.html',datum=data)

@app.route('/about')
def about():
    return render_template('about.html')





