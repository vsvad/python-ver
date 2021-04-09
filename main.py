from flask import *
import requests
import re
import os
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python ' + sys.version + ' on ' + sys.platform + '</h1>'


@app.route('/latest.txt')
def latest():
    page = requests.get('https://python.org/', headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"}).text
    where = page.find('<h1>Python ') + 11
    if where == 10:
        return Response('Unknown', mimetype="text/plain")
    return Response(page[where:where+5], mimetype="text/plain")


app.run(host='0.0.0.0', port=os.environ.get('PORT', 8000))
