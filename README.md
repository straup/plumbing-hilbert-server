# plumbing-hilbert-server

A simple Flask-based HTTP pony for encoding and decoding (x,y,z) triples in to points on a Hilbert walk.

## Usage

To start the server:

	$> gunicorn --chdir /usr/local/plumbing-hibert-server/flask/

To encode a triple:

	$> curl 'http://127.0.0.1:8000/encode/122419304/37764832/1268809061'
	{
		"i": 4104889776306142950229134145,
		"x": 122419304,
		"y": 37764832,
		"z": 1268809061
	}

To decode a Hilbert point:

	$> curl 'http://127.0.0.1:8000/decode/4104889776306142950229134145'
	{
		"i": 4104889776306142950229134145,
		"x": 122419304,
		"y": 37764832,
		"z": 1268809061
	}

## See also

* http://www.tiac.net/~sw/2008/10/Hilbert/
