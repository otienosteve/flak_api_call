from flask import render_template
from . import app
from urllib import request,parse
import json

@app.route('/')
def home():
    params={
    "api_key":"rJM3VmADEJHGZR2wo6gnANb9TzYVhX5c",
    "limit":"5",
    "q":"willsimith"
    }
    qrstring=parse.urlencode(params)
    base_url='https://api.giphy.com/v1/gifs/trending?'
    req=request.urlopen(base_url+qrstring)
    resp=req.read()
    apires=json.loads(resp)
    data=apires["data"]
    data2="https://media2.giphy.com/media/rVzvUgOpJlQkS06ZMO/giphy.gif?cid=57eecaf543os4uu6ngzm1zfka75hq27sn0vnmtaxcobldw02&rid=giphy.gif&ct=g"
    # for i in data:
    #     if i!=" ":
    #         data2+=i

    return render_template('index.html',datum=data)

@app.route('/about')
def about():
    return render_template('about.html')





