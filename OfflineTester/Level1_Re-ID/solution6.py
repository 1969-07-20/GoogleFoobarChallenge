'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/46853104/can-this-solution-to-the-google-foobar-re-id-be-more-efficient (Austin T)"


import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

primes = ''

for i in range(2,21000,1):
    if len(primes) < 10005:
        if is_prime(i):
            primes = primes + str(i)
    else:
        break

def answer(n):
    re_id = primes[n:n+5:1]
    return(re_id)
