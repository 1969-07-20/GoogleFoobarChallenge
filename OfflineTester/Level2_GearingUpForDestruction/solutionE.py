'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/40465866/google-foobar-gearing-up-for-destruction/45626410#45626410 (thiswind)"


#  Mod:
#  - explicitly import reduce if running under Python 3


from fractions import Fraction

import sys
if 3 <= sys.version_info[0]:
    from functools import reduce

def solution(p):
    n = len(p)

    if n >= 2:
        r0_n = -2 * (p[n - 1] + reduce(
            lambda a, b: a + b, [0] + [(-1)**i * 2 * p[i]
                                       for i in range(n - 2, 0, -1)]) + (-1)**(n-1)*p[0])

        r0_d = 1 + ((n+1) % 2)*2

        if r0_n < r0_d:
            return [-1, -1]

        r = ['NAN'] * n
        r[0] = float(r0_n) / float(r0_d)
        for i in range(1, n):
            r[i] = p[i] - p[i - 1] - r[i - 1]
            if r[i] < 1:
                return [-1, -1]

        r0 = Fraction(r0_n, r0_d)
        r0.limit_denominator()
        
        return [r0.numerator, r0.denominator]

    return [-1, -1]
