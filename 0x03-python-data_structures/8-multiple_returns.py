#!/usr/bin/python3
def multiple_returns(sentence):
        ch = len(sentence)
        if ch == 0:
            i = None
        else:
            i = sentence[0]
        return (ch, i)
