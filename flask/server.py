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

@app.route('/encode/<int:x>/<int:y>/<int:z>', methods=['GET'])
@app.route('/encode/<int:x>/<int:y>', methods=['GET'])
@cross_origin(methods=['GET'])
def mk_hilbert(x, y, z=None):

    if not z:
        z = int(time.time())

    coords = (x, y, z)
    i = hilbert.Hilbert_to_int(coords)

    rsp = flask.jsonify(x=x, y=y, z=z, i=i)
    return rsp

@app.route('/decode/<int:i>', methods=['GET'])
@cross_origin(methods=['GET'])
def mk_int(i):

    (x, y, z)= hilbert.int_to_Hilbert(i, 3)

    rsp = flask.jsonify(x=x, y=y, z=z, i=i)
    return rsp

if __name__ == '__main__':
    debug = True	# sudo make me a CLI option
    app.run(debug=debug)
