'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.oasys.net/posts/google-foobar-programming-challenge"


#  Mod:
#  - Made importing gcd() from fractions or math dependent on Python version
#  - Replace calls to 'xrange()' with calls to 'range()'
#  - Fixed problem where Fraction(a,b) wanted rational arguments
#  - Fixed error "TypeError: unsupported operand type(s) for +: 'range' and 'range'" when running under Python 3.
#  - Forced numerators in return list to ints.


from fractions import Fraction
import sys
if 3 == sys.version_info[0]:
    from math import gcd
else:
    from fractions import gcd


def fraction(numerator, denominator=1):
    return 0 if numerator == 0 else Fraction(Fraction(numerator).limit_denominator(), Fraction(denominator).limit_denominator())


def subtract(a, b):
    # subtract matrix b from a
    #n = xrange(len(a))
    n = range(len(a))
    return [[a[i][j] - b[i][j] for j in n] for i in n]


def identity(m):
    # identity matrix for matrix m
    #n = xrange(len(m))
    n = range(len(m))
    return [[1 if i == j else 0 for j in n] for i in n]


def multiply(a, b):
    # multiply matrices a x b
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]


def invert(a):
    b = identity(a)
    #or d in xrange(len(a)):
    for d in range(len(a)):
        to1 = fraction(1, a[d][d])
        #or j in xrange(len(a)):
        for j in range(len(a)):
            a[d][j] *= to1
            b[d][j] *= to1
        for i in list(range(len(a)))[0:d] + list(range(len(a)))[d + 1 :]:
            to0 = a[i][d]
            #or j in xrange(len(a)):
            for j in range(len(a)):
                a[i][j] = a[i][j] - to0 * a[d][j]
                b[i][j] = b[i][j] - to0 * b[d][j]
    return b


def lcm(a):
    # least common multiple for array
    for i, x in enumerate(a):
        lcm = x if i == 0 else lcm * x // gcd(lcm, x)
    return lcm


def solution(m):
    """
    This problem describes an absorbing Markov Chain.

    The provided data is almost in canonical form, P.  With this matrix,
    we can then use its properties to determine B, the probabilities of
    ending up in a particular absorbing (terminal) state.
              _       _
             |         |
             |  Q   R  |
        P =  |         |
             |  0   I  |
             |_       _|

                        -1
        B =  ( I  -  Q )   * R
    """

    terminal = [not any(row) for row in m]

    if terminal.count(True) == 1:
        return [1, 1]

    p = [
        [
            1
            if terminal[state] and state == next_state
            else fraction(prob, sum(m[state]))
            for next_state, prob in enumerate(probs)
        ]
        for state, probs in enumerate(m)
    ]

    q = [
        [p[i][j] for j, is_terminal in enumerate(terminal) if not is_terminal]
        for i, is_terminal in enumerate(terminal)
        if not is_terminal
    ]

    r = [
        [p[i][j] for j, is_terminal in enumerate(terminal) if is_terminal]
        for i, is_terminal in enumerate(terminal)
        if not is_terminal
    ]

    # probabilities for starting in state 0
    b0 = multiply(invert(subtract(identity(q), q)), r)[0]

    common = lcm([x.denominator for x in b0])

    return [int(x.numerator * common / x.denominator) for x in b0] + [common]

