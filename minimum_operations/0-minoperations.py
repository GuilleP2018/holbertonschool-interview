#!/usr/bin/python3
""" Module that calculates the minimum number of operations """


def minOperations(n):
    """ Function to calculate the minimum number of operations"""
    if n <= 1:
        return 0
    ops = 0
    i = 2
    while i <= n:
        if n % i == 0:
            ops += i
            n = n / i
        else:
            i += 1
    return ops
