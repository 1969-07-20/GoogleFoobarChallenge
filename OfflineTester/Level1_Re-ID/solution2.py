'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ankit-kaushal/Re-ID/blob/master/re_id.py"


import math
def prime(a):
    if (a % 2 == 0) and (a > 2):
        return False
    return all(a % i for i in range(3, int(math.sqrt(a)) + 1, 2))

primes = ''

for i in range(2,21000):
    if len(primes) < 10000:
        if prime(i):
            primes = primes + str(i)
    else:
        break

def solution(a):
    reid = primes[a:a+5:1]
    return(reid)
