#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    length = len(sentence)
    t = (length, first)
    if length == 0:
        first = None
    else:
        return t
