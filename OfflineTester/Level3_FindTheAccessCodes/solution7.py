'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/simran029/GoogleFoobarChallenge/blob/master/Solution.py"


def solution(l):
    if len(l)<3:
        return 0
    ans = [0]*len(l)
    x = len(l)-2
    res=0
    while x>=0 :
        y = 0
        z = len(l)-1
        div = 0
        mul = 0
        while x>y:
            if l[x]%l[y]==0:
                div +=1
            y +=1
        while x<z:
            if l[z]%l[x]==0:
                mul +=1
            z -=1
        res= res + mul*div
        x -=1
            
    return res
