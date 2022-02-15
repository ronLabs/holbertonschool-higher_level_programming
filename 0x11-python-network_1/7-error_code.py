#!/usr/bin/python3
""" esto es un comentario """
import requests
from sys import argv

if __name__ == '__main__':
    url = requests.get(argv[1])
    if url.status_code >= 400:
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)
