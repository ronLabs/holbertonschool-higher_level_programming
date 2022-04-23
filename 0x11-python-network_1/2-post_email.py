#!/usr/bin/python3
""" script that takes in a URL and an email,
    sends a POST request to the passed URL
    with the email as a parameter, and displays
    the body of the response (decoded in utf-8) """
from urllib import request
from urllib import parse
from sys import argv


if __name__ == '__main__':
    url, email = argv[1:]
    data = {'email': email}

    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = request.Request(url, data)

    with request.urlopen(req) as res:
        _bytes = res.read()
        print(_bytes.decode('utf-8'))
