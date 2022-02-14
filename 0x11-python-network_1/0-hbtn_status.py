#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
    -You must use the package urllib
    -You must use a with statement """
import urllib.request


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        req_pag = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(req_pag)))
    print("\t- content: {}".format(req_pag))
    print("\t- utf8 content: {}".format(req_pag.decode('utf-8')))
