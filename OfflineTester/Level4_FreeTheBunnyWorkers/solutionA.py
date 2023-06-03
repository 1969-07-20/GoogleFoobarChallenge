'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gitlab.com/DevAlone/google_foobar_solutions/-/blob/master/level%204/Free%20the%20Bunny%20Prisoners/main.py"


import itertools

"""
num_buns - bunnies I have [1, 9]
num_required - bunnies required to open one door [0, 9]
"""
def answer(num_buns, num_required):
    if num_buns < num_required:
        raise Exception('Oh no, we are DOOMED! There are too few bunnies!')

    # get minimum combination such that we wouldn't give more keys
    # than necessary to open any door by any num_required bunnies
    num_required = num_buns - num_required + 1

    bunnies = []

    # just create bunnies
    for i in range(num_buns):
        bunnies.append([])

    keysCombinations = \
        list(itertools.combinations(range(num_buns), num_required))
    combinationsCount = len(keysCombinations)

    for i in range(combinationsCount):
        for bunnyIndex in keysCombinations[i]:
            bunnies[bunnyIndex].append(i)

    return bunnies

