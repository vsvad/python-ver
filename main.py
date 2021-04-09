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
    soup = BeautifulSoup(requests.get('https://python.org/').text, 'html.parser')
    tags = soup.find_all('a')
    for tag in tags:
        match = re.search('^\d\.\d(\.\d)?', a['href'])
        if match:
            span = match.span()
            result = match.string[span[0]:span[1]]
            return Response(result, mimetype="text/plain")
    return Response('Unknown', mimetype="text/plain")


app.run(host='0.0.0.0', port=os.environ.get('PORT', 8000))
