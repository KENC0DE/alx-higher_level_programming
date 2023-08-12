#!/usr/bin/python3
def multiple_returns(sent):
    lng = len(sent)
    fc = sent[0] if sent is not None else 'None'
    return lng, fc
