#!/usr/bin/python3
"""
    sends a request to the URL and displays
    the value of the variable X-Request-Id in
    the response header
"""


import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    got = requests.get(url)

    print(got.headers.get('X-Request-Id'))
