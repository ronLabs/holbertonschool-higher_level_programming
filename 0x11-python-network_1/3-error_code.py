#!/usr/bin/python3
""" script that takes in a URL,
    sends a request to the URL and displays
    the body of the response (decoded in utf-8). """
from urllib import request
from urllib import parse
from urllib import error
from sys import argv


if __name__ == '__main__':
    try:
        url = request.Request(argv[1])
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
