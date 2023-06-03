'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://govanify.com/post/foobar/#en-route-salute"


def answer(s):

    if(len(s) > 100 or len(s) < 1):
        raise ValueError('Height is outside of bounds')
    
    s = list(s.replace("-",""))
    left = []
    right = []
    res=0

    for i in range(0,len(s)):
        if s[i] == '<':
            left.append(i)
        if s[i] == '>':
            right.append(i)

    for i in right:
        for y in left:
            if i < y:
                res+=1
    for i in left:
        for y in right:
            if y < i:
                res+=1
                
    return res 
