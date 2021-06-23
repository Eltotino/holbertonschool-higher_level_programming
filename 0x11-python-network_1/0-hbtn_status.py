#!/usr/bin/python3
"""UrlLibRequest"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as path:
        body = path.read()
    print("Body response:")
    print("\t- type: {}".format(body))
    print("\t- content: {}".format(body))
    print("\t- utf-8 content: {}".format(body))
