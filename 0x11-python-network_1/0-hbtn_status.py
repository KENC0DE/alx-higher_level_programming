#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

url = "https://alx-intranet.hbtn.io/status"

r = urllib.request.Request(url)
with urllib.request.urlopen(r) as rps:
    got = rps.read()

f_rps = f"""Body response:
    - type: {type(got)}
    - content: {got}
    - utf8 content: {got.decode('utf-8')}"""

print(f_rps)
