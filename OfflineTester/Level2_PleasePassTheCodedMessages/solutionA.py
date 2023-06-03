# -*- coding: utf-8 -*-

'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = u"https://yueyue200830.github.io/2022/04/30/Google-Foo-Bar挑战"


def solution(l):
    x = [0 for i in range(10)]
    
    s = 0
    for i in l:
        x[i] += 1
        s += i
    diff = s % 3
    if diff != 0:
        # cut 1 char
        for i in range(10):
            if x[i] > 0 and i % 3 == diff:
                x[i] -= 1
                diff = 0  # set to zero
                break
        
        if diff != 0:
            # cut 2 char
            for i in range(10):
                if x[i] > 0:
                    x[i] -= 1
                    for j in range(10):
                        if x[j] > 0 and (i + j) % 3 == diff:
                            x[j] -= 1
                            diff = 0
                            break
                    if diff == 0:
                        break
                    x[i] += 1
        
    if diff != 0:
         return 0
    
    result = 0
    for i in range(9, -1, -1):
        while x[i] > 0:
            result = result * 10 + i
            x[i] -= 1
    return result

