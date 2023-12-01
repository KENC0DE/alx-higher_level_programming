#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
"""


import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    got = requests.get(url)

    print('Body response:')
    print(f'\t- type: {type(got.headers["content-type"])}')
    print(f'\t- content: {got.text}')
