#!/usr/bin/python3
"""UrlLibRequest"""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as path:
        header = path.getheader('X-Request-Id')
    print(header)
