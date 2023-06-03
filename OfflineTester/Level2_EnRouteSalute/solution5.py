'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/argcag/foobar1/blob/main/foobar1.py"


#foobar 1
#algorithmic approach:
#if we have a list (">---<><") we only need to consider 1 direction of movement
#(for this example i will only look at the left facing arrows, and simply check how many right facing arrows are on the left of each, add 2 for each).

def solution(hallway):
    salutes = 0
    for i in range(0,len(hallway)): #range = the whole list
        if hallway[i] == "<":
            for j in range(0,i): #range = the list up to where the left facing arrow is
                if hallway[j] == ">": 
                    salutes += 2
    return salutes
