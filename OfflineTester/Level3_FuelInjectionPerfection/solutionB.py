'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rudisimo/google-foobar/blob/master/solutions/fuel_injection_perfection/solution.py"


#  Mod:
#  - Fixed problem where long() is not defined by defining a new function long() if the python version is 3.


import sys
if 3 == sys.version_info[0]:
    def long(a):
        return int(a)

def answer(n):
    n = long(n)

    # define lookup table
    lookup_table = { long(1): long(0), long(2): 1 }

    def calculate_steps(n):
        # return memoized value in lookup table
        if n in lookup_table:
            return lookup_table[n]

        # handle safety control limitations (optimized)
        if n & 1:
            # odd numbers have an extra operation due to constraint
            lookup_table[n] = min(calculate_steps((n + 1) >> 1) + 2,
                                  calculate_steps((n - 1) >> 1) + 2)
        else:
            # even numbers add a single operation
            lookup_table[n] = calculate_steps(n >> 1) + 1

        return lookup_table[n]

    # calculate number of steps
    return calculate_steps(n)
