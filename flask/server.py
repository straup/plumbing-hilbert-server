#!/usr/bin/env python

import flask
from flask_cors import cross_origin 

import hilbert
import time
import urlparse

import logging
logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    # return flask.render_template("index.html")
    endpoint = 'http://fixme/'

    spec = {
        'encode': {
            'description': 'encode an x,y,x triple in to a point on a Hilbert walk',
            'example': endpoint + 'encode/{X}/{Y}/{Y}',
        },
        'decode': {
            'description': 'decode a point on a Hilbert walk in to a x,y,z triple',
            'example': endpoint + 'decode/{I}',
        }
    }

    rsp = flask.jsonify(spec)
    return rsp

@app.route('/encode', methods=['GET'])
@cross_origin(methods=['GET'])
def mk_hilbert():

    qs = flask.request.query_string
    qs = urlparse.parse_qs(qs)

    x = qs.get('x', None)
    y = qs.get('y', None)
    z = qs.get('z', None)

    if not x:
        flask.abort(400)

    if not y:
        flask.abort(400)

    if not z:
        z = int(time.time())

    x = int(x[0])
    y = int(y[0])

    coords = (x, y, z)
    i = hilbert.Hilbert_to_int(coords)

    rsp = flask.jsonify(x=x, y=y, z=z, i=i)
    return rsp

@app.route('/decode', methods=['GET'])
@cross_origin(methods=['GET'])
def mk_int():

    qs = flask.request.query_string
    qs = urlparse.parse_qs(qs)

    i = qs.get('i', None)

    if not i:
        flask.abort(400)

    i = int(i[0])

    (x, y, z)= hilbert.int_to_Hilbert(i, 3)

    rsp = flask.jsonify(x=x, y=y, z=z, i=i)
    return rsp

if __name__ == '__main__':
    debug = True	# sudo make me a CLI option
    app.run(debug=debug)
