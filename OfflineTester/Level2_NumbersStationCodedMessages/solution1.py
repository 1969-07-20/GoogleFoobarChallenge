'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level2_NumbersStationCodedMessages/numbersStationCodedMessages.py"


"""  This file computes solutions to the "Numbers Station Coded Messages"
challenge.

The strategy here is simple.  A sublist is maintained.  If the numbers in the
list are arranged from left to right, the sublist either grows on the right or
shrinks on the left.  The sublist grows if the sum in the sublist is less than
the target sum t.  The sublist shrinks if the sum in the sublist is greater
than t.  If the sum in the sublist is equal to t, then the answer has been
found.

These operations ensure that the sublist moves from left to right and that the
first sublist that sums to t is found.
"""


def solution(l, t):
    """Function solution(l,t) computes solutions to the "Numbers Stations Coded
    Messages" challenge.  Given list of numbers l and total t this function
    finds the first sublist of l that sums to t.
    """

    idx0 = 0
    idx1 = 0

    tot = l[0]

    while True:

        #  Case tot is less than t:  Add one element to the front of the list
        if tot < t:

            #  Return failure if an element cannot be added to front of list
            if idx1 == len(l) - 1:
                return [-1, -1]

            #  Add element to front of the list
            idx1 += 1
            tot += l[idx1]

        #  Case tot is greater than t:  Remove one element from back of list
        elif tot > t:

            #  Return failure if removing an element makes the list zero length
            if idx0 == len(l) - 1:
                return [-1, -1]

            #  Drop element from end of list
            tot -= l[idx0]
            idx0 += 1

        #  Case tot is equal to t:  Return answer
        else:
            return [idx0, idx1]
