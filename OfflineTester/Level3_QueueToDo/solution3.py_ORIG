'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://govanify.com/post/foobar/#queue-to-do"


def xor(a, b):
    if(a%2==0):
        xor_rotation = [b, 1, b+1, 0]
    else:
        xor_rotation= [a, a^b, a-1, (a-1)^b]
    return xor_rotation[(b-a)%4]

def answer(start, length):
    res=0
    for i in range(0, length):
        res ^= xor(start+(length*i), start+(length*i)+(length-i)-1)
    return res
