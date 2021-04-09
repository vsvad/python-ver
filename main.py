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
    page = requests.get('https://python.org/').text
    where = page.find('<h1>Python ') + 11
    if where == 10:
        return Response('Unknown', mimetype="text/plain")
    return Response(page[where:where+5], mimetype="text/plain")


app.run(host='0.0.0.0', port=os.environ.get('PORT', 8000))
