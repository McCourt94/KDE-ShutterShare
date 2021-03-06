from flask import Flask, Response, json, render_template, jsonify
from flask import request
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from subprocess import Popen, PIPE, STDOUT
import os
import shlex

app = Flask(__name__)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/python/solr/',methods=['GET'])
@crossdomain(origin='*')
def solr():
    tag = request.args.get('tag')
    cmd = 'python solr.py %s' % tag
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    output = p.stdout.read()
    print output
    return output

@app.route('/python/spatialsearch/',methods=['GET'])
@crossdomain(origin='*')
def geo():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    radius = request.args.get('radius')
    intr = int(radius)
    cmd = 'python spatialsearch.py %s %s %s' % (latitude, longitude, intr)
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    output = p.stdout.read()
    print output
    return output

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)