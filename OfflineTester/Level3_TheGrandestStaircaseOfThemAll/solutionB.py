'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rudisimo/google-foobar/blob/master/solutions/the_grandest_staircase_of_them_all/solution.py"


#  Mod:
#  - Replaced xrange() with range()


import json
import math

def calculate_steps(n):
    # pad size
    size = n + 1

    # create zero-filled matrix
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    # base value is always padded and skipped
    matrix[0][0] = 1
    for prev in range(1, size):
        for left in range(0, size):
            matrix[prev][left] = matrix[prev - 1][left]
            if left >= prev:
                matrix[prev][left] += matrix[prev - 1][left - prev]

    return matrix[n][n] - 1

def answer(n):
    return calculate_steps(n)
