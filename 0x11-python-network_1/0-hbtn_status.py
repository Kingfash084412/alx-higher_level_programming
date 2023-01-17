#!/usr/bin/python3

from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("{}{}".format("\t- type: ", type(html)))
        print("{}{}".format("\t- content: ", html))
        print("{}{}". format("\t- utf8 content: ", html.decode('utf-8')))
