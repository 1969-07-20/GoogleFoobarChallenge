'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ggarredondo/foo.bar-hey-i-already-did-that/blob/main/solution.py"


def decimal_to_base(n, b):
    if b == 10 or n == 0:
        return str(n)
    digits = ''
    while n:
        digits += str(n % b)
        n //= b
    return digits[::-1]


def lambda_algorithm(n, b):
    k = len(n)
    string = ''.join(sorted(n))
    x = int(string[::-1], b)
    y = int(string, b)
    z = abs(x - y)
    n = decimal_to_base(z, b)
    while len(n) < k:
        n = '0' + n
    return n


# Floyd's cycle detection algorithm
def floyd(f, x0, b):
    tortoise = f(x0, b)
    hare = f(f(x0, b), b)
    while tortoise != hare:
        tortoise = f(tortoise, b)
        hare = f(f(hare, b), b)

    lam = 1
    hare = f(tortoise, b)
    while tortoise != hare:
        hare = f(hare, b)
        lam += 1

    return lam


# Precondition: n must represent a nonnegative integer where 2 <= k <= 9 and 2 <= b <= 10
def solution(n, b):
    return floyd(lambda_algorithm, n, b)
