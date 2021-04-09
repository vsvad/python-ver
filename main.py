from flask import *
import requests
import re
import os
import sys
from bs4 import BeautifulSoup

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
    return page[where:where+5]


app.run(host='0.0.0.0', port=os.environ.get('PORT', 8000))
