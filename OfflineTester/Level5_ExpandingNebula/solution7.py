'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://projects.govanify.com/govanify/foobar/-/blob/master/expanding_nebula.py"


"""
The hard part of this challenge was figuring out how to make it in the time
limit, much like the old XOR challenge. This one though was on another
optimization technique, memoization(I see what you did there Google, challenges
using the skills you ask for interviews on your website).
Hashing the entire list would have been too long, even as a tuple, so instead we
had to be clever and use another trick: building an history of all the moves that
happened.
This allows us, given a pair of row and column a and b, to avoid having to do
extreme amount of recursive computation to get a result, as long as an history
of the last (past grid row + current move) moves is saved.
The rest of the problem is fairly easy: we recursively try out all possible
combinations for this grid and save the number of correct ones we could get.
"""
def answer(state, a=0, b=0, past=0, solutions=0, history=0):
    if(past==0):
        past=[[True] * (len(state[0])+1) for i in range(len(state)+1)]
        solutions = {}
        history = []

    if(b==len(state[0])+1):
        return True 

    res=0
    index=((a,b), tuple(history[-(len(state)+2):]))
    if index in solutions:
        return solutions[index]

    for cell in [True, False]:
        # either all True(c[0][0] and 1 cell) or all False (!c[0][0] and !1 cell)
        if (not a or not b) or len(set([((past[a][b-1] + past[a-1][b]
            + past[a-1][b-1] + cell)==1), state[a-1][b-1]]))==1:
                history.append(cell)
                past[a][b] = cell
                res+=answer(state, a=(a+1)%(len(state)+1),
                        b=b+(a+1)//(len(state)+1), past=past,
                        solutions=solutions, history=history)
                history.pop()

    solutions[index]=res
    return res

