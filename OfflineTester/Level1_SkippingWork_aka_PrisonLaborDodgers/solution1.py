'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level1_SkippingWork/skippingWork.py"


"""  This file computes solutions to the "Skipping Work" challenge.

The strategy implemented in this solution is to create sorted versions of the
two lists and then compare them element-wise until the first mismatch.  The
unique ID will be the mismatching element that came from the longer list.
"""


def solution(x, y):
    """Function solution(x, y) computes solutions to the "Skipping Work"
    challenge.  Given lists x and y of worker IDs, solution() identifies
    the ID which is present in only one of these lists and returns it.
    """

    #  Create list s and l such that:
    #  - s is the sorted version of the shorter list and
    #  - l is the sorted version of the longer list.
    #  Note:  since l is longer, we know it will have the unique ID.
    if len(x) < len(y):
        s = sorted(x)
        l = sorted(y)
    else:
        l = sorted(x)
        s = sorted(y)

    #  Pop heads of lists until unique ID is found
    while len(s) > 0:
        s_element = s.pop(0)
        l_element = l.pop(0)

        if s_element != l_element:
            return l_element

    #  If we get here the unique ID was the last ID of l
    return l[0]
