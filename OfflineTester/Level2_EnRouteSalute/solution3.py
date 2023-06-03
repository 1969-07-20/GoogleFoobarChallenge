'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://towardsdatascience.com/google-foobar-challenge-level-2-7a021f625c1"


import re
def solution(s):
    no_dash = re.sub('-', '', s)

    # find number of salutes for walkers going right
    answer = 0
    for ind, direction in enumerate(no_dash):
        if direction == '>':
            people_in_front = no_dash[ind:]
            left_walkers = people_in_front.count('<')

            answer += left_walkers * 2

    return answer
