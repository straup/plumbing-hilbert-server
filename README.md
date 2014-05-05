# plumbing-hilbert-server

A simple Flask-based HTTP pony for encoding and decoding (x,y,z) triples in to points on a Hilbert walk.

## Usage

To start the server:

	$> gunicorn --chdir /usr/local/plumbing-hibert-server/flask/ server:app

_Strictly speaking you don't need to use [gunicorn](http://www.gunicorn.org) but I like it. Note that the use of the `--chdir` flag requires using gunicorn version 18 or higher._

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

## Notes and gotchas

Automatic conversion of "things" to integers (for example an IP address) is not currently supported. This includes stuff like negative numbers.

## See also

* http://www.tiac.net/~sw/2008/10/Hilbert/
* https://spacetimeid.appspot.com/

## See also because... I'm not sure why but it seems relevant

* https://github.com/client9/snowflake2time
