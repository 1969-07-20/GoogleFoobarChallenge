'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level3_DoomsdayFuel/doomsdayFuel.py"


from fractions import Fraction

import sys
if sys.version_info[0] == 2:
    from fractions import gcd
else:
    from math import gcd
from functools import reduce

"""
The code in this file computes answers to the Doomsday Fuel challenge.  The
function solution(m) is called with argument 'm' which is a matrix holding
the number of observations of the number of transitions of the ore from one
state to another state.

At its core this challenge is an absorbing Markov chain.  From the matrix of
observations one can estimate the probabilities of the transitions of the ore
among the various states.

The procedure for solving absorbing Markov chains is well-established.  The
application of this procedure to this challenge is outlined below.

Step 1:  Identify the absorbing states and rearrange the transition matrix T
into a standard form T'.  T' is arranged such that it has sub-matrices R, Q,
I, and 0, such that T' = [[ R, Q ], [ I, 0 ]].  I is the identity matrix, 0 is
a zero matrix which mathematically capture the fact that once in the absorbing
state, ore does not transition to any other state.  R, and Q are sub-matrices
which respectively capture the probabilities of ore in a non-absorbing state
transitioning into a non-absorbing state and absorbing state.  NOTE:  In this
solution, T' is not explicitly created, but rather only R and Q.

Step 2:  Find "fundamental matrix" F which is the inverse matrix of (I - Q).
NOTE:  This I is a different identity matrix from the one in Step 1.  This
I is of the same size as Q.

Step 3:  Compute F*R.  This matrix gives the fraction of ore which starts in
each of the non-absorbing state which ultimately ends up in each of the
absorbing states.  Since in this challenge all ore starts in state S0, the
first row of FR gives the answer to this challenge.
"""


#  From https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-the-least-common-multiple
def lcm(arr):
    """Function lcm() finds the least common multiple of an array of integers
    arr."""

    l = reduce(lambda x, y: (x * y) // gcd(x, y), arr)
    return l


def compute_inverse(m):
    """Function compute_inverse() computes the inverse of the matrix m using
    Gaussian elimination.  NOTE:  This implementation does not handle singular
    matrices or performs row exchange.  This implementation is good enough for
    the Doomsday Fuel challenge, but it is not robust enough for production."""

    #  Create augmented matrix
    m_aug = []

    for idx0 in range(len(m)):
        m_row = []

        for idx1 in range(len(m[idx0])):
            m_row.append(m[idx0][idx1])

        for idx1 in range(len(m[idx0])):
            if idx0 == idx1:
                m_row.append(Fraction(1))
            else:
                m_row.append(Fraction(0))

        m_aug.append(m_row)

    #  Perform forward elimination
    for idx0 in range(len(m_aug)):

        #  Divide the row by the leading coefficient to set it to 1
        weight = m_aug[idx0][idx0]

        for idx2 in range(idx0, len(m_aug[idx0])):
            m_aug[idx0][idx2] = m_aug[idx0][idx2] / weight

        #  Eliminate this row from subsequent rows
        for idx1 in range(idx0 + 1, len(m_aug)):
            weight = m_aug[idx1][idx0] / m_aug[idx0][idx0]

            for idx2 in range(idx0, len(m_aug[idx0])):
                m_aug[idx1][idx2] = m_aug[idx1][idx2] - weight * m_aug[idx0][idx2]

    #  Perform backward elimination
    for idx0 in reversed(range(len(m_aug))):
        for idx1 in reversed(range(idx0)):
            weight = m_aug[idx1][idx0] / m_aug[idx0][idx0]

            for idx2 in range(idx0, len(m_aug[idx0])):
                m_aug[idx1][idx2] = m_aug[idx1][idx2] - weight * m_aug[idx0][idx2]

    #  Extract inverse matrix
    m_inv = []

    for idx0 in range(len(m)):
        m_row = []

        for idx1 in range(len(m)):
            m_row.append(m_aug[idx0][len(m) + idx1])

        m_inv.append(m_row)

    return m_inv


def solution(m):
    """Function solution() computes solutions to the Doomsday Fuel Challenge.
    as defined by the transition matrix m."""

    num_states = len(m)

    #  Identify the absorbing states and denominators of fractions
    absorbing_states = [True] * num_states
    sum_weights = [0] * num_states

    for idx0 in range(len(m)):
        for idx1 in range(len(m[idx0])):
            if 0 != m[idx0][idx1]:
                absorbing_states[idx0] = False

                sum_weights[idx0] += m[idx0][idx1]

    #  Handle corner case where initial state is absorbing
    if 0 == sum_weights[0]:
        result = [0] * (len(m) + 1)

        result[0] = 1
        result[-1] = 1

        return result

    #  Form R and (I-Q)
    R = []
    ImQ = []

    for idx0 in range(num_states):
        if not absorbing_states[idx0]:
            r_row = []
            q_row = []

            for idx1 in range(num_states):
                if absorbing_states[idx1]:
                    num = m[idx0][idx1]
                    den = sum_weights[idx0]

                    r_row.append(Fraction(num, den))
                else:
                    if idx0 == idx1:
                        num = sum_weights[idx0] - m[idx0][idx1]
                    else:
                        num = -m[idx0][idx1]

                    den = sum_weights[idx0]

                    q_row.append(Fraction(num, den))

            R.append(r_row)
            ImQ.append(q_row)

    #  Handle case where there are no absorbing states
    if 0 == len(ImQ):
        return [1]

    #  Form F = (I-Q)^-1
    F = compute_inverse(ImQ)

    #  Form FR
    FR = []

    for idx0 in range(len(F)):
        fr_row = []

        for idx1 in range(len(R[0])):
            val = Fraction(0, 1)

            for idx2 in range(len(F[idx0])):
                val = val + F[idx0][idx2] * R[idx2][idx1]

            fr_row.append(val)

        FR.append(fr_row)

    #  Find denominator of result
    dens = []

    for idx1 in range(len(FR[0])):
        dens.append(FR[0][idx1].denominator)

    den = lcm(dens)

    #  Create the list holding the solution
    result = []

    for idx1 in range(len(FR[0])):
        num = FR[0][idx1].numerator * (den // gcd(den, FR[0][idx1].denominator))

        result.append(num)

    result.append(den)

    #  Make normal return
    return result
