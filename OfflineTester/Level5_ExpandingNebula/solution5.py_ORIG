'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/lotabout/891621ae8a01d8e512afd4b5254516b4"


def generate(c1,c2,bitlen):
    a = c1 & ~(1<<bitlen)
    b = c2 & ~(1<<bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

from collections import defaultdict
def build_map(n, nums):
    mapping = defaultdict(set)
    nums = set(nums)
    for i in range(1<<(n+1)):
        for j in range(1<<(n+1)):
            generation = generate(i,j,n)
            if generation in nums:
                mapping[(generation, i)].add(j)
    return mapping

def answer(g):
    g = list(zip(*g)) # transpose
    nrows = len(g)
    ncols = len(g[0])

    # turn map into numbers
    nums = [sum([1<<i if col else 0 for i, col in enumerate(row)]) for row in g]
    mapping = build_map(ncols, nums)

    preimage = {i: 1 for i in range(1<<(ncols+1))}
    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[(row, c1)]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    ret = sum(preimage.values())

    return ret
