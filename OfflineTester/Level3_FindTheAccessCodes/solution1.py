'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level3_FindTheAccessCodes/findTheAccessCodes.py"



"""  This file implements a solution to the 'Find the Access Codes' puzzle.

Concept of operation:
    The following observations are key to this solution to the Find the Access
    Codes puzzle:

    This puzzle potentially has very high time and/or space complexity.  The
    largest number of combinations possible is the case when the list is maximum
    length (2000) and all the numbers are the same.  In that case all possible
    combinations of 3 indices are "lucky triples".  The number of solutions is
    2000 choose 3 or 1331334000.  Computing all lucky triples is susceptible to
    exceeding the maximum time allowed and avoiding computations by memoizing
    intermediate results is susceptible to exceeding the maximum allowed memory.

    One observation is the foundation to this solution's strategy to mitigating
    the time and space complexity issues of the puzzle.  Consider the set of
    triples (i, j0, k) where i < j0 < k, involving a fixed j0.
        - Let K be the set of k0 such that l[j0] divides l[j0].
        - Let I be the set of i0 such that l[i0] divides l[j0].
    Since all combinations of i0 from I and k0 from K form lucky triples, the
    number of lucky triples involving j0 is equal to the number of elements in I
    times the number of elements in K.

    The algorithm in this solution is simple.  It loops over j finding the
    number of lucky triples involving j.  For each j it loops over i < j
    finding the number of i such that l[i] divides l[j] and then loops over
    k > j such and finds the number of k such that l[j] divides l[k].  It then
    adds the product of these two the cumulative number of lucky triples found.


Time and space complexity of the solution:

    Overall, this solution has O(N^2) time complexity and O(N) space complexity
    where N is the number of elements in the list l.  The O(N^2) time complexity
    comes from the fact that the number of outer loops (j) is O(N) and within
    each of the outer loops O(N) work is performed.  This algorithm requires
    a fixed number of scalars to store intermediate and final results resulting
    in O(1) space complexity beyond the input array with requires O(N) space.

Assumptions/restrictions:
    None beyond the limitations stated in the problem statement.

This solution is completely of my own conception and execution.
"""

def solution(l):
    # Handle corner case where list is less than length 3
    if len(l) < 3:
        return 0

    count = 0

    #  Loop over all possible middle indices (j) in triples (i,j,k)
    for j in range(1, len(l)-1):

        # Count number of elements before element j which divide l[j] evenly
        count_bef = 0
        for i in range(0, j):
            if 0 == l[j] % l[i]:
                count_bef += 1

        # Count number of elements after element j which are multiples of l[j]
        count_aft = 0
        for k in range(j+1, len(l)):
            if 0 == l[k] % l[j]:
                count_aft += 1

        # The number of lucky triples involving l[j] is the product of
        # count_bef and count_aft
        count += (count_bef * count_aft)

    return count
