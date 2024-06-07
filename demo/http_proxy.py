from flask import Flask, request
import json
import redis
import requests
import re
import time
import hashlib
import os
import socket
import traceback

import base64

import logging
import logging.config
logging.config.fileConfig('logger.conf', disable_existing_loggers=False)
LOGGER = logging.getLogger()

app = Flask(__name__)

HTTP_SESSION = requests.Session()
HTTP_SESSION.mount('http://', requests.adapters.HTTPAdapter(pool_connections=1000, pool_maxsize=3000, max_retries=3))
HTTP_SESSION.mount('https://', requests.adapters.HTTPAdapter(pool_connections=1000, pool_maxsize=3000, max_retries=3))


def update_netloc(url, new_netloc):
    return re.sub(r'^http[s]*://[^/]+', new_netloc, url)

def send_to_newloc(request, new_netloc):
    url = request.url
    new_url = update_netloc(url, new_netloc)
    #print(f"ori url: {url}")
    #print(f"new url: {new_url}")
    #print(request.method)

    headers = dict(request.headers)
    del headers['Host']
    #print(headers)
    #print('data: {}'.format(request.get_data()))
    if request.method == 'POST':
        resp = HTTP_SESSION.post(new_url, headers=headers, data=request.get_data(), timeout=10)
    elif request.method == 'GET':
        resp = HTTP_SESSION.get(new_url, headers=headers, timeout=10)
    return resp.text, resp.status_code, dict(resp.headers)

NEW_NETLOCS = ['http://localhost:8080', 'http://az-apis-fcm-in.telta.in']
#NEW_NETLOCS = ['http://localhost:8080']

def send_to_newlocs(request):
    headers_json_str = json.dumps(dict(request.headers), separators=(',', ':'), ensure_ascii=False)
    LOGGER.info('url: %s, method: %s, header: %s, data: %s', request.url, request.method, headers_json_str, request.get_data(as_text=True))
    result = None
    for new_netloc in NEW_NETLOCS:
        result = send_to_newloc(request, new_netloc)
    return result

@app.route('/')
def default():
    return ""

@app.route('/sp/vivo_count', methods=['GET', 'POST'])
def vivo_count():
    LOGGER.info(request)
    return send_to_newlocs(request)

@app.route('/vivo/addressingData', methods=['GET', 'POST'])
def push_addressingdata():
    return send_to_newlocs(request)

@app.route('/fcmReport/', methods=['GET', 'POST'])
def fcm_report():
    return send_to_newlocs(request)


@app.route('/fcmReportIntl/', methods=['GET', 'POST'])
def fcm_report_intl():
    return send_to_newlocs(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)