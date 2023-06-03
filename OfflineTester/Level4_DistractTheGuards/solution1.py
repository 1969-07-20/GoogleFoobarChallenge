'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level4_DistractTheGuards/distractTheGuards.py"


#  Mod:
# - Made importing gcd() from fractions or math dependent on Python version
# - For compatibility with Python 3, Wrapped range() in a list() when creating
#   the 'mapping[]' array.


"""  This file implements a solution to the 'Distract the Guards' puzzle.

Description of algorithm:
    The following observations are key to this solution to the Distract the
    Guards puzzle:

    0)  The sum of the number of bananas stays constant.  If a and b (a < b)
        are the numbers of bananas at the beginning of a round, during the
        round a bananas get transferred from the guard with b bananas to the
        guard with a.  No bananas are created or destroyed.  Furthermore,
        the game has the memoryless property:  the outcome of a round depends
        solely on the numbers of bananas at the start of the round and not what
        has happened before.  The sum of the bananas is constant throughout
        the whole game and the outcome of the game is solely determined by
        the sum of the number of bananas.  (More on this in Observation 2.)

    1)  Let a be the number of bananas the first guard in a game starts off
        with and b be the number of bananas the second guard starts off with.
        Furthermore, let gcf be the greatest common factor of a and b.  When
        the guards play the banana game, the number of bananas the guards have
        will always be some multiple of gcf.  Imagine that instead of
        individual bananas, the guards play the game with baskets of bananas
        where each basket has gcf bananas.  Whole baskets of bananas will be
        exchanged every round.

        In summary, the outcome of a game with (a,b) bananas is the same as a
        game with (a/gcf,b/gcf) bananas, or an (a,b) game is equivalent to a
        (a/gcf,b/gcf) game.

    2)  Assume any starting configuration of bananas is divided by the gcf.
        The game terminates if, and only if, the number of bananas/baskets is a
        power of 2, i.e. a/gcf + b/gcf = 2^n, for some positive integer value
        n.  Otherwise, the game is guaranteed to repeat some cycle forever and
        never terminate.  This allows us to determine the outcome of any pairing
        of guards very quickly.  In fact it is so quick I found it advantageous
        to determine the the outcome of all possible pairings of guards at the
        beginning.  Determining the outcome by simulating a game with an
        arbitrary number of bananas can take quite long time if one of the
        numbers is large.

        To substantiate this observation, note that a game terminates only when
        the numbers of bananas become equal.  If a and b are the number of
        bananas at the beginning of a round and the game terminates that round,
        we know that 2a = b - a or b = 3a or the total number of bananas is 4a.
        This means that 4 = 2^2 is a factor of the sum of the bananas in any
        terminating game, which from Observation 1) above is equivalent to a
        game with a bananas.

        Applying the (2a = b - a) constraint for termination along with the
        greatest common factor equivalence recursively leads us to the two
        configurations of (1,1) and (2,2).  But greatest common factor
        equivalence means that (2,2) is equivalent to (1,1).  Therefore, all
        terminating games are equivalent to the (1,1) game and the
        factorization of the sum of bananas in those games consist solely of
        factors of 4 (=2^2) and 2.

        The sum of the bananas in all terminating games are powers of 2.

    This solution to the Distract the Guards puzzle has two phases.  In the first
    phase, the above observations are used to quickly construct a 2D array whose
    elements record the outcome of the banana game for every possible pairings of
    the N guards.

    The second phase of the solution tries to transform an arbitrary initial
    configuration of match-ups of guards into a configuration which result in
    the fewest games terminating.  The solution does this by iteratively swapping
    pairs of guards between games which convert terminating match-ups of guards
    into non-terminating match-ups. The method of implementation is to use a
    permutation of guards and match the guards in the first half against the
    corresponding guards in the second half.  Swapping guards is done by
    exchanging the position of pairs of guards in the permutation.

    NOTE:
        When using the number of matches which do not terminate as a metric,
        this solution's method of determining the minimum number of guards
        depends on the metric space being convex under the operation of
        swapping pairs of guards between games.  In other words, this solution
        depends on being able to improve the goodness metric via swapping a
        single pair of guards at every step when transforming an arbitrary
        matching of guards to an optimum matching.

        I am not convinced this is always possible for all configurations. But I
        believe the fact that a match will not terminate for the vast majority
        of combinations of numbers of bananas means there is HIGH PROBABILITY
        this solution's method will find one of the optimum matches.

        Swapping pairs of guards can be thought of as applying a cyclic
        permutation of length two to those (two) guards.  The strategy I have in
        mind to find the/an optimum configuration of guards with certainty for
        all configurations is to find and apply cyclic permutations of guards of
        arbitrary length.  For example, if at some point the guards A, B, C, X,
        Y, Z are matched as (A,X), (B,Y) and (C,Z), I was going to extend the
        current solution to be able to find and apply a cyclic permutation of
        length three A -> B -> C ->  to transform the above matches to (C,X),
        (A,Y), (B,Z).

        This is getting into the realm of combinatorics.  One can imagine that
        the time and code complexity increasing very rapidly.  Fortunately, the
        current solution's high probability of finding the optimum matching was
        good enough for this puzzle's test cases.


Time and space complexity of the solution:

    Overall, this solution has O(N^3) time complexity and O(N^2) space complexity
    where N is the number of guards.  An algorithm of O(N^3) time complexity is
    nothing to brag about.  But the problem statement limits N to 100, keeping
    us out of the realm where O(N^3) complexity becomes prohibitive.

    The solution has two phases of operation.  In the first phase, the solution
    constructs a 2D array where the entry in the ith row and jth column has a
    value of -1 or 1 depending on whether or not the match between the ith and
    jth guard terminates.  The second phase iteratively improves the matchings
    of guards until the matchings can't be improved anymore.

    Let N be the number of guards.  For each of the O(N^2) entries in the 2D array
    calculating gcd(a,b), calculating a/gcf + b/gcf and bit shifting require O(1)
    time and space.  Therefore, determining the outcomes of all pairs of guards
    requires O(N^2) time and space complexity.  (A dynamic programming approach
    could be used to potentially reduce this complexity, but since the problem
    statement upper bounds N to 100, the time space resources are so modest that
    it does not justify the increased code complexity of a dynamic program
    solution.)

    In the second phase, the matchings of guards is iteratively improved.  The
    iterations stop when an iteration does not improve.  Since there are N/2
    pairings and the number of bad pairings decreases for every iteration but
    the last, the number of iterations is O(N).  Each iteration examines each
    of the O(N) pairings.  If a pairing is bad it scans each of the O(N) other
    guards looking for a swap which will replace the bad match with a good one.
    Thus O(N^2) work is performed for each of the O(N) iterations resulting in
    O(N^3) complexity.

Assumptions/restrictions:
    None beyond the limitations stated in the problem statement.

This solution is completely of my own conception and execution.

"""

#rom fractions import gcd
import sys
if sys.version_info[0] == 2:
    from fractions import gcd
else:
    from math import gcd


def determine_outcomes(bananas):
    """Compute the outcome of all possible pairings of guards and return the
    result in the 2D array 'outcome'."""


    #  Get the number of guards from the number of entries in the bananas list
    num_guards = len(bananas)

    #  Make 2D array with outcomes of each pairing of guards
    outcome = [[0 for j in range(num_guards)] for i in range(num_guards)]

    #  Determine outcome for each possible pairings of guards
    for i in range(num_guards):
        outcome[i][i] = -1

        for j in range (i+1, num_guards):

            #  Get the number of bananas each guard in this match begins with
            m = bananas[i]
            n = bananas[j]

            #  Remove greatest common factor
            greatest_common_factor = gcd(m, n)

            if greatest_common_factor > 1:
                m //= greatest_common_factor
                n //= greatest_common_factor

            #  Form the sum of the number of bananas
            sum = m + n

            #  Bit-shift the sum right until the right-most bit is bit 1
            while (sum % 2) == 0:
                sum = sum >> 1

            #  If the sum was a power of two, the result after bit shifting is
            #  exactly 1
            if sum != 1:
                outcome[i][j] = 1
                outcome[j][i] = 1
            else:
                outcome[i][j] = -1
                outcome[j][i] = -1

    return outcome


def query_outcome(i, j, state):
    """Follow the current permutation map to determine the guards at positions
    i and j and return the corresponding entry in the array 'outcome'."""

    #  Determine which guards are currently in positions i and j
    m = state['mapping'][i]
    n = state['mapping'][j]

    #  Return outcome for this pair of guards
    return state['outcome'][m][n]


def get_min_guards(bananas, outcome):
    """Given the 'outcome' 2D array which has the outcome for all possible
    pairings of guards, determine the minimum number of guards whose games
    will terminate."""

    #  NOTE:  A permutation array will be used for the guards.  Guards in
    #  the first half of the permutation will be matched with guards in
    #  the second half of the permutation.  Pairs of guards will be swapped
    #  in the array until the number of matches which terminate is minimized.

    #  Determine the number of guards
    num_guards = len(bananas)

    #  Determine number of matches
    num_matches = num_guards // 2

    #  Make array that maps guard order in matches to initial guard order
    mapping = list(range(num_guards))

    #  Make a data structure holding state
    state = {'outcome': outcome, 'mapping': mapping, 'bananas': bananas}


    #  Swap pairs of guards until cannot/need not improve anymore
    i0 = 0
    j0 = num_matches


    #  Scan matches looking for bad pairings, continue until cannot improve
    swap = True
    while swap:
        swap = False

        #  Scan matches from beginning to end; remove matches that terminate
        i, j = i0, j0

        while i < num_matches:

            #  If this match is bad, look for the guard to swap with to best
            #  improve pairings
            if query_outcome(i, j, state) < 0:

                #  Scan list from bottom to top best entry to swap with
                #  (Start at bottom to maximize probability of removing a bad
                #  match that would be encountered later.)
                k = 2 * num_matches - 1

                b_best = -2 * num_guards
                k_best = -1

                while (k >= 0):

                    #  Determine the index that k pairs with
                    if k >= num_matches:
                        l = k - num_matches
                    else:
                        l = k + num_matches

                    #  Calculate benefit of swapping i with k
                    if (k != i) and (k != j):
                        o0 = query_outcome(i, j, state) + \
                             query_outcome(k, l, state)
                        o1 = query_outcome(k, j, state) + \
                             query_outcome(i, l, state)

                        benefit = o1 - o0

                        #  Record if this improves on previous best
                        if b_best < benefit:
                            b_best = benefit
                            k_best = k

                    k -= 1

                #  If best swap improves has positive benefit, do it
                if b_best > 0:
#                   mapping[i], mapping[k_best] = mapping[k_best], mapping[i]
                    temp = mapping[i]
                    mapping[i] = mapping[k_best]
                    mapping[k_best] = temp

                    swap = True

            #  If there are an odd number of guards, the one at the end needs
            #  special handling because it is not paired with any other guards
            if ((num_guards % 2) == 1):

                #  If the (i,j) match is still bad, consider swapping with the
                #  singleton guard at the end
                if query_outcome(i, j, state) < 0:
                    z = num_guards - 1

                    #  Swap i and z if it improves things
                    if (query_outcome(z, j, state) > 0):
                        mapping[i], mapping[z] = mapping[z], mapping[i]

                        swap = True

                    #   Swap j and z if it improves things
                    elif (query_outcome(i, z, state) > 0):
                        mapping[j], mapping[z] = mapping[z], mapping[j]

                        swap = True

            #  Done with current pair of guards, increment indices to next pair
            i += 1
            j += 1


    #  Count the number of good pairings
    i, j = i0, j0

    num_good = 0
    while i < num_matches:
        if query_outcome(i, j, state) > 0:
            num_good += 1

        i += 1
        j += 1


    #  Return the minimum number of guards not distracted by banana game
    return num_guards - 2 * num_good


def solution(bananas):

    #  Handle corner case of 1 guard
    if 1 == len(bananas):
        return 1

    #  Sort bananas by increasing value
    bananas = sorted(bananas)

    #  Determine outcome for each possible pairing of guards
    outcome = determine_outcomes(bananas)

    #  Get the minimum number of guards not distracted by banana game
    min_guards = get_min_guards(bananas, outcome)


    return min_guards
