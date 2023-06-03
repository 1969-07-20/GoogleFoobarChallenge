'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/oneshan/foobar/blob/master/dodge_the_lasers/solution.py"


#  Mod:
#  - Fixed problem where long() is not defined by defining a new function long() if the python version is 3.
#  - Increased precision to 201 digits in order to correctly calculate answer for 200th Pell number + 1


# beatty sequence sum
# https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
from decimal import Decimal, getcontext
getcontext().prec = 201
sqrt2m1 = Decimal(2).sqrt() - 1

import sys
if 3 == sys.version_info[0]:
    def long(a):
        return int(a)

def answer(str_n):
    n = long(str_n)

    def s(n):
        if n == 1:
            return 1
        if n < 1:
            return 0
        n1 = long(sqrt2m1 * n)
        return n * n1 + n * (n + 1) // 2 - n1 * (n1 + 1) // 2 - s(n1)

    return str(s(n))
