'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://pages.cs.wisc.edu/~shrey/2020/08/10/google-foobar.html"


def solution(pegs):
    prop_sol = 2*(sum(pegs[1::2]) - sum(pegs[::2])) + pegs[0]

    if len(pegs) % 2 == 0:
        prop_sol = 2* (prop_sol - pegs[-1])
        if prop_sol/3 < 1:
            return [-1,-1]
        if prop_sol % 3 == 0:
            ret_val = [prop_sol/3,1]
        else:
            ret_val = [prop_sol,3]
    else:
        prop_sol = 2* (prop_sol + pegs[-1])
        if prop_sol < 1:
            return [-1,-1]
        else:
            ret_val = [prop_sol, 1]
    last_gear = ret_val[0]/ret_val[1]
    for i in range(len(pegs)-1):
        last_gear = pegs[i+1]-pegs[i] - last_gear
        if last_gear < 1:
            return [-1,-1]
    return ret_val
