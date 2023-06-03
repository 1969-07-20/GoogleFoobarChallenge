'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/pijel/assorted-algos/blob/master/foobar_5.py"


#  Mod:
#  - Made importing gcd() from fractions or math dependent on Python version


import sys
if 3 == sys.version_info[0]:
    from math import gcd
else:
    from fractions import gcd


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return a * b // (gcd(a, b))


def parti(n):
    p = [[[]], [[1]]]
    while len(p) < n + 1:
        new_e = []
        for i in range(1, len(p) // 2 + 1):
            for j in p[i]:
                for k in p[len(p) - i]:
                    b = j + k
                    b.sort()
                    if b not in new_e:
                        new_e.append(j + k)
        new_e.append([len(p)])
        p.append(new_e)
    return p[-1]


fact_table = [1,
              1,
              2,
              6,
              24,
              120,
              720,
              5040,
              40320,
              362880,
              3628800,
              39916800,
              479001600,
              6227020800,
              87178291200,
              1307674368000,
              20922789888000,
              355687428096000,
              6402373705728000,
              121645100408832000,
              2432902008176640000,
              51090942171709440000,
              1124000727777607680000,
              25852016738884976640000,
              620448401733239439360000,
              15511210043330985984000000,
              403291461126605635584000000,
              10888869450418352160768000000,
              304888344611713860501504000000,
              8841761993739701954543616000000]


def new_fact(n):
    if n < 30:
        return fact_table[n]
    return n * new_fact(n - 1)


def num_cycles(n, k):
    return new_fact(n) // (k * (new_fact(n - k)))


def binom(n, k):
    return new_fact(n) // ((new_fact(k)) * new_fact(n - k))


def to_term(lis):
    size = sum(lis)
    powers = [0] * (size)
    for i in lis:
        powers[i - 1] += 1
    coeffecient = 1
    n = size
    for i in lis:
        coeffecient *= num_cycles(n, i)
        n = n - i
    for c in powers:
        coeffecient = coeffecient // new_fact(c)
    return [coeffecient, powers]


def get_cycle_index(n):
    k = parti(n)
    poly = []
    for i in k:
        poly.append(to_term(i))
    return poly


def multiply(term1, term2):
    t = len(term1[1])
    l = len(term2[1])
    mult = [term1[0] * term2[0], [0] * (t * l)]
    for i in range(len(term1[1])):
        for k in range(len(term2[1])):
            mult[1][lcm(i + 1, k + 1) - 1] += term1[1][i] * term2[1][k] * gcd(i + 1, k + 1)
    return mult


def cycle_product(n, m):
    a = get_cycle_index(n)
    b = get_cycle_index(m)
    prod = []
    for i in a:
        for k in b:
            prod.append(multiply(i, k))
    return prod


def answer(n, m, c):
    product = cycle_product(n, m)
    s = 0
    for k in product:
        s += k[0] * (c ** (sum(k[1])))
    return str(s // (new_fact(m) * new_fact(n)))
