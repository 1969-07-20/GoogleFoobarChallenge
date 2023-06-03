'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/fox0088/The-Grandest-Staircase-Of-Them-All/blob/master/GrandestStaircaseOfThemAll.py"


#  Mod:
#  - Use Python's built-in sum() function instead of numpy's.

def solution(N): 
    memo = [[0 for x in range(N+2)] for y in range(N+2)]
    memo[3][2] = memo[4][2] = 1   #setting base cases
  
    for y in range (5, N+1) :
        memo[y][2] = memo[y-2][2] + 1   #@2 steps: # of staircases inc by 1
                                        #when n inc by 2
        for x in range (3, y + 1) :
            memo[y][x] = memo[y-x][x-1] + memo[y-x][x]
            if memo[y][x]==0: break  #no more steps possible beyond this
    return sum(memo[N])
