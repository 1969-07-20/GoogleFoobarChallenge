'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/59525299/google-foobar-challenge-power-hungry-failing-test-no-3-hidden-out-of-5-test (Atharva Kulkarni)"


def solution(xs):

    if(xs.count(0) == len(xs)):
        return(str(0))

    if(len(xs) == 1 and len([n for n in xs if n < 0]) == 1):
        return(str(xs[0]))

    if(len([n for n in xs if n < 0]) == 1 and xs.count(0) == len(xs)-1):
        return(str(0))

    Val = 1

    for i in xs:
        if (i != 0 and i <= 1000):
            Val *= i

    if Val < 0:
        BigNeg = max([n for n in xs if n < 0])
        Val = Val/BigNeg

    return(str(int(Val)))
