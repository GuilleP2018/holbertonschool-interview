#!/usr/bin/python3
""" validUTF8 """


def validUTF8(data):
    """Check if a list of integers represents a valid UTF-8 encoding."""
    num_bytes = 0
    for num in data:
        binary_representation = format(num, '#010b')[-8:]
        if num_bytes == 0:
            for bit in binary_representation:
                if bit == '0': break
                num_bytes += 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not binary_representation.startswith('10'):
                return False
        num_bytes -= 1
    return num_bytes == 0
