#!/usr/bin/python3

from sys import argv
from urllib.request import urlopen, Request

if __name__ == "__main__":

    req = Request(argv[1])

    with urlopen(req) as response:

        allinfo = response.info()

        print(allinfo.get('X-Request-Id'))
