#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not "":
        t = (len(sentence), sentence[0])
    else:
        t = (len(sentence), None)
    return t

