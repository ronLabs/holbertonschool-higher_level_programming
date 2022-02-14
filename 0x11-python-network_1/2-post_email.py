#!/usr/bin/python3
""" script that takes in a URL and an email,
    sends a POST request to the passed URL
    with the email as a parameter, and displays
    the body of the response (decoded in utf-8) """
from urllib import request
from urllib import parse
from sys import argv


if __name__ == '__main__':
    req_pag = argv[1]
    send_email = {"email": argv[2]}
    post_pag = parse.urlencode(send_email).encode("utf-8")
    req_req = request.Request(req_pag, post_pag)

    with request.urlopen(req_req) as response:
        data = response.read().decode("utf-8")
    print(data)
