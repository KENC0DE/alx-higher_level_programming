#!/usr/bin/python3
"""
    sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""


import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as resp:
            got = resp.read()
            dcd = got.decode('utf-8')

        print(dcd)
    except urllib.error.HTTPError as er:
        print(f"Error code: {er.code}")
