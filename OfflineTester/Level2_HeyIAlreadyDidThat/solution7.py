# -*- coding: utf-8 -*-

'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/malikbabayev95/Hey-I-Already-Did-That-Google/blob/main/solution.py"


def solution(n,b):
    id = []
    number = str(n)
    x = ''
    y = ''
    z = ''
    while number not in id:
        id.append(number)
        s = sorted(str(number))
        x = ''.join(s[::-1])
        y = ''.join(s)
        z = IntToBase((BaseToInt(int(x),b) - BaseToInt(int(y),b)) , b)
        z_length = len(str(z))
        n_length = len(number)
        if z_length<n_length:
            zero = '0'*(n_length-z_length)
            z = zero + str(z)
        number = z
    return len(id)-id.index(number)

def BaseToInt(number, base):
    number = str(number)
    base = int(base)
    known_digits = '0123456789'
    value  = { ch:val for val,ch in enumerate(known_digits) if val<base }
    if number[0]=='-':
        sign = -1
        number = number[1:]
    else:
        sign = 1
    total = 0
    for d in number:
        try:
            total = total*base + value[d]
        except KeyError:
            if d in known_digits:
                raise ValueError("'{1}' - base-də '{0}' rəqəmi mümkün deyil .".format(d, base))
            else:
                raise ValueError("'{0}' rəqəminin dəyəri tapılmadı".format(d))

    return sign*total

def IntToBase(x, base):
    digs = '0123456789'
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)
