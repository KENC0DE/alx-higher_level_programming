#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as rps:
        got = rps.read()

    print("Body response:")
    print(f"\t- type: {type(got)}")
    print(f"\t- content: {got}")
    print(f"\t- utf8 content: {got.decode('utf-8')}")
