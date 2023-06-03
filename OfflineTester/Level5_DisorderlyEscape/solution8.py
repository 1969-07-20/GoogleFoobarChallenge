'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rajakodumuri/Google-Foobar.git"


#  Mod:
#  - Added import of gcd()
#  - Convert answer to string upon return to caller.


"""
    Disorderly Escape
    =================

    Oh no! You've managed to free the bunny prisoners and escape Commander Lambdas exploding space station,
    but her team of elite starfighters has flanked your ship. If you dont jump to hyperspace, and fast,
    youll be shot out of the sky!

    Problem is, to avoid detection by galactic law enforcement, Commander Lambda planted her space station
    in the middle of a quasar quantum flux field. In order to make the jump to hyperspace, you need to know the
    configuration of celestial bodies in the quadrant you plan to jump through. In order to do *that*, you
    need to figure out how many configurations each quadrant could possibly have, so that you can pick the
    optimal quadrant through which youll make your jump.

    There's something important to note about quasar quantum flux fields' configurations: when drawn on a star grid,
    configurations are considered equivalent by grouping rather than by order. That is, for a given set of configurations,
    if you exchange the position of any two columns or any two rows some number of times, youll find that all of those
    configurations are equivalent in that way - in grouping, rather than order.

    Write a function answer(w, h, s) that takes 3 integers and returns the number of unique, non-equivalent configurations
    that can be found on a star grid w blocks wide and h blocks tall where each celestial body has s possible states.
    Equivalency is defined as above: any two star grids with each celestial body in the same state where the actual
    order of the rows and columns do not matter (and can thus be freely swapped around). Star grid standardization means
    that the width and height of the grid will always be between 1 and 12, inclusive. And while there are
    a variety of celestial bodies in each grid, the number of states of those bodies is between 2 and 20, inclusive.
    The answer can be over 20 digits long, so return it as a decimal string. The intermediate values can also be large,
    so you will likely need to use at least 64-bit integers.

    For example, consider w=2, h=2, s=2. We have a 2x2 grid where each celestial body is either in state 0
    (for instance, silent) or state 1 (for instance, noisy). We can examine which grids are equivalent by swapping
    rows and columns.

    00
    00

    In the above configuration, all celestial bodies are "silent" - that is,
    they have a state of 0 - so any swap of row or column would keep it in the same state.

    00 00 01 10
    01 10 00 00

    1 celestial body is emitting noise - that is, has a state of 1 - so swapping rows and columns can put it in any of
    the 4 positions. All four of the above configurations are equivalent.

    00 11
    11 00

    2 celestial bodies are emitting noise side-by-side. Swapping columns leaves them unchanged, and swapping rows
    simply moves them between the top and bottom. In both, the *groupings* are the same: one row with two bodies
    in state 0, one row with two bodies in state 1, and two columns with one of each state.

    01 10
    01 10

    2 noisy celestial bodies adjacent vertically. This is symmetric to the side-by-side case, but it is different
    because there's no way to transpose the grid.

    01 10
    10 01

    2 noisy celestial bodies diagonally.  Both have 2 rows and 2 columns that have one of each state,
    so they are equivalent to each other.

    01 10 11 11
    11 11 01 10

    3 noisy celestial bodies, similar to the case where only one of four is noisy.

    11
    11

    4 noisy celestial bodies.

    There are 7 distinct, non-equivalent grids in total, so answer(2, 2, 2) would return 7.

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java

    Test cases
    ==========

    Inputs:
        (int) w = 2
        (int) h = 2
        (int) s = 2
    Output:
        (string) "7"

    Inputs:
        (int) w = 2
        (int) h = 3
        (int) s = 4
    Output:
        (string) "430"
"""

from fractions import *
from copy import *

import sys
if 3 == sys.version_info[0]:
    from math import gcd
else:
    from fractions import gcd

def expand(frac, terminal):
    for term in terminal:
        term[0] *= frac
    return terminal

def multiply(sub, terminal):
    terminal = deepcopy(terminal)
    for term in terminal:
        alreadyIncluded = False
        for a in term[1]:
            if a[0] == sub:
                alreadyIncluded = True
                a[1] += 1
                break
        if not alreadyIncluded:
            term[1].append([sub, 1])
    return terminal

def add(terminala, terminalb):
    terminal = terminala + terminalb
    if len(terminal) <= 1:
        return terminal
    for i in range(len(terminal) - 1):
        for j in range(i + 1, len(terminal)):
            if set([(a[0], a[1]) for a in terminal[i][1]]) == set([(b[0], b[1]) for b in terminal[j][1]]):
                terminal[i][0] = terminal[i][0] + terminal[j][0]
                terminal[j][0] = Fraction(0, 1)
    return [term for term in terminal if term[0] != Fraction(0, 1)]

def lcm(a, b):
    return abs(a * b) / gcd(a, b) if a and b else 0

petCache = {}

def petCycleSimm(n):
    global petCache
    if n == 0:
        return [[Fraction(1.0), []]]
    if n in petCache:
        return petCache[n]
    terminal = []
    for l in range(1, n + 1):
        terminal = add(terminal, multiply(l, petCycleSimm(n - l)))
    petCache[n] = expand(Fraction(1, n), terminal)
    return petCache[n]

def petCycleProdA(cyca, cycb):
    alist = []
    for ca in cyca:
        lena = ca[0]
        insta = ca[1]
        for cb in cycb:
            lenb = cb[0]
            instb = cb[1]
            vlcm = lcm(lena, lenb)
            alist.append([vlcm, (insta * instb * lena * lenb) / vlcm])
    if len(alist) <= 1:
        return alist
    for i in range(len(alist) - 1):
        for j in range(i + 1, len(alist)):
            if alist[i][0] == alist[j][0] and alist[i][1] != -1:
                alist[i][1] += alist[j][1]
                alist[j][1] = -1
    return [a for a in alist if a[1] != -1]

def petCycleSimmNM(n, m):
    indA = petCycleSimm(n)
    indB = petCycleSimm(m)
    terminal = []
    for flatA in indA:
        for flatB in indB:
            newterminal = [[flatA[0] * flatB[0], petCycleProdA(flatA[1], flatB[1])]]
            terminal.extend(newterminal)
    return terminal

def substitute(term, v):
    total = 1
    for a in term[1]:
        total *= v**a[1]
    return (term[0] * total)

def answer(w, h, s):
    terminal = petCycleSimmNM(w, h)
    total = 0
    for term in terminal:
        total += substitute(term, s)
    return str(int(total))
