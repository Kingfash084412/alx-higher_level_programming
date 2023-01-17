#!/usr/bin/python3

from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":

    url = argv[1]
    value = {'email': argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:

        html = response.read().decode('utf-8')
        print(html)
