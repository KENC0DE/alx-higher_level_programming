#!/usr/bin/python3
"""
    sends a POST request to the passed URL
    with the email as a parameter, and displays
    the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    params = {'email': sys.argv[2]}
    url = sys.argv[1]
    
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as resp:
        got = resp.read()
        dcd = got.decode('utf-8')

    print(dcd)
