'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ken-power/Foobar_Challenge/blob/main/Level_5/9_DodgeTheLasers/solution.py"


#  Mod:
#  - Increased precision to 201 digits in order to correctly calculate answer for 200th Pell number + 1


import unittest

from decimal import Decimal, getcontext


def beatty_sequence(alpha, n):
    """
    A Beatty sequence (or homogeneous Beatty sequence) is the sequence of integers found by taking the floor of the
    positive multiples of a positive irrational number. Beatty sequences are named after Samuel Beatty, who wrote about
    them in 1926.

    From The Online Encyclopedia of Integer Sequences:
         Beatty sequence: a(n) = floor(n*sqrt(2))

    Since at each step n is approximately multiplied by sqrt(2)-1, the arguments decrease exponentially.
    For n=10**100 (which is our given upper limit) we need approximately ceil(100 log 10 / log(sqrt(2) -1)) = 262 steps
    to complete the recursion.

    https://en.wikipedia.org/wiki/Beatty_sequence
    https://mathworld.wolfram.com/BeattySequence.html
    https://oeis.org/A001951
    https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s/2053713#2053713

    :param alpha: some irrational positive number, e.g., square root of 2
    :param n: defines the range 1 to n
    :return: the Beatty sequence of n
    """
    if n == 1:
        return 1
    if n < 1:
        return 0

    if alpha >= 2:
        beta = alpha - 1
    else:
        beta = alpha

    # From the Beatty Sequence proof:
    # n' = floor((alpha - 1) * n)
    n_prime = int((alpha - 1) * n)

    # S(alpha, n) = (n * n') + n(n+1)/2 - n'(n' + 1)/2 - S(beta,n')
    p = n * n_prime  # Let p = (n * n')
    q = n * (n + 1) // 2  # Let q = n'(n' + 1)/2
    r = n_prime * (n_prime + 1) // 2  # Let r = n'(n' + 1)/2

    # S(alpha, n) = p + q - r - S(beta,n')
    return p + q - r - beatty_sequence(beta, n_prime)


def solution(s):
    """
    Given the string representation of an integer n, for every number i in the range 1 to n, add up all of
    the integer portions of i*sqrt(2).

    :param s: string representation of an integer n
    :return: the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string
    """
    # check the input string is a valid length
    min_length = 1
    max_length = 201

    if len(s) < min_length or len(s) > max_length:
        return ''

    # need to handle integers between 1 and 10^100, so up to 101 decimal places of precision
    # The Python default is 28 significant figures
    # https://www.geeksforgeeks.org/setting-precision-in-python-using-decimal-module/
    getcontext().prec = max_length

    n = int(s)
    alpha = Decimal(2).sqrt()
    sequence = beatty_sequence(alpha, n)

    return str(int(sequence))
