#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
    -You must use the package requests """
import requests


if __name__ == '__main__':
    url = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.text))
