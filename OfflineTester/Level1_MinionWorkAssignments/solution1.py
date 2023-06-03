'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level1_MinionWorkAssignments/minionWorkAssignments.py"


"""  This file computes solutions to the "Minion Work Assignments" challenge.

Two passes are made over the list of work assignments.  The first pass creates
a count of each type of assignment.  The second pass copies work assignments
from the input list of those assignments which do not exceed the maximum
number of occurrences.
"""


def solution(data, n):
    """Function solution(data,n) computes solutions to the "Minion Work
    Assignments" challenge.  Given list of work assignments n and max
    occurrences n, this function returns a list where assignments which
    exceed the max occurrences are removed.
    """

    #  Step one:  Count the number of occurrences of each assignment
    count = {}
    for item in data:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    #  Step two:  Construct output list with excessive occurrences removed
    result = []
    for item in data:
        if count[item] <= n:
            result.append(item)

    return result
