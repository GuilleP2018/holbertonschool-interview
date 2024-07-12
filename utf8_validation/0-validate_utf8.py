#!/usr/bin/python3
""" validUTF8 """

def validUTF8(data):
    """ validUTF8
    Returns true if data is a valid UTF-8 encoding, else returns false
    """
    if not data:
        return False
    for i in data:
        if i < 0 or i > 255:
            return False
    return True
