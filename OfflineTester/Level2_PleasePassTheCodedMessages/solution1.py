'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level2_PleasePassTheCodedMessages/pleasePassTheCodedMessages.py"


from functools import reduce

"""  This file implements a solution to the 'Please Pass the Coded Messages'
challenge.

It would be straight-forward to solve this by forming all possible permutations
of digits, testing each permutation if it is divisible by three and recording
the largest.

The number of permutations to be tested increases as the factorial of the number
of digits.  The problem statement limits the number of digits to 9 and as a
result the number of permutations to be tested is 9! = 362880, trivial on
modern computers.  However, if the number of digits (plates) were increased just
to 20, the number of permutations to check becomes non-trivial.

More importantly, where is the fun in the straight-forward solution?

The solution presented here approaches the problem differently and as a result,
the time complexity of the is dominated by the O(n log n) time required to sort
the digits.

The following observations form the foundation for the solution implemented
here:

1)  Given a number N which is divisible by 3, all numbers formed by rearranging
    the digits of N (in its base 10 representation) are also divisible by 3.
    The reason for this is closely related to the "Casting out of Nines" method
    of checking arithmetic calculations.

    The above claim is due to the fact that for every non-negative power of 10,
    that number minus 1 is divisible by 3.  Stated differently, for any n >= 0,
    10^n - 1 = 99...99.  It is trivial to see from inspection that 99...99 is
    divisible by 3.  What this means is that 10^n mod 3 = 1.  A result of this
    is that for all non-negative powers of n and digit values d, 0 <=d<= 9,

    (d * 10^n) mod 3 = (d * 10^(n-1)) mod 3 = (d * 10^0) mod 3 = d mod 3.

    I.e. it doesn't matter in which position a digit appears, its remainder mod
    3 is the same.  Therefore when determining if a number is divisible by 3,
    we don't need to consider the position of the digits appear, all we need to
    consider is the sum of the remainders after dividing the digits individually
    is divisible by 3.

2)  A consequence of the above, is that, given a set of digits l, to form
    numbers divisible by 3 from subsets of l, all we have to do is pick subsets
    such that the sum of their residues mod 3 is 0.  Once we have such a subset,
    we are free to arrange the digits any way we want and the we are assured the
    resulting number is divisible by 3.

    The crux of the implementation here is to find the subset of digits which
    make up the answer and then arranging them correctly.

3)  We are seeking the largest number that can be formed from the digits in l
    that is divisible by three.  These digits have the following attributes.

    a)  The sum of their remainders mod 3 is 0.  This was established above.
    b)  As few as possible digits in l are excluded.  This is because the
        smallest number that can be formed with n digits (i.e. a 1 and n-1
        0's) is larger than ALL numbers that can be formed from fewer than n
        digits.
    c)  We can determine which digits to exclude based on which residue class
        the sum is and the residue classes of the individual digits.

        If the sum of residues of the digits mod 3 is 0, NO digits need to be
        excluded. If the sum mod 3 is non-zero then the sum mod 3 can be made to
        equal 0 by excluding either one or two digits, provided digit(s) from
        the appropriate residue class is(are) available for exclusion.

        i)  We never want to exclude a digit from residue class 0 because doing
            so will have no impact on the residue class of the sum.  Therefore,
            we only want to exclude digits from residue classes 1 and 2.
        ii)  If there is one or more digits belonging to the same residue class
            as the sum of the digits, then excluding one digit from this class
            will result in the sum having a remainder 0.
        ii)  If we cannot achieve the desired result by excluding one digit,
            then we can have the desired result by excluding two digits from the
            other non-zero residue class:

            (1 + 1) mod 3 = 2
            (2 + 2) mod 3 = 1

        Once we determine which residue classes one or more digits need to be
        excluded, we know which digits to exclude:  the smallest one(s).
    d)  Once we have determined which digits are in the answer, determining
        their order to make the largest number possible from them is trivial:
        We order the digits from largest to smallest.

The solution presented here is extremely fast.  As stated above, the operation
with the greatest time complexity (sorting the digits) which is O(n log n)
where n is the number of digits.

The following is a list of the operations making up the implementation here and
the time complexity of each.
1)  Sort the digits:  O(n log n)
2)  Determine the residue class of all the digits:  O(n)
3)  Determine number of digits to exclude from residue classes 1 and 2:  O(1).
4)  Form the output value from the non-excluded digits:  O(n)

Therefore, the overall time complexity is O(n log n) in the number of digits.
The space complexity is O(n).
"""


def solution(digits_in):
    """Function solution() determines the largest number which can be formed
    from the list of digits in 'digits_in' that is divisible by 3.  If no
    number can be formed that is divisible by 3, then the function returns 0.
    """

    #  Make lists of the digits in each of the residue classes of 3
    residues = [[], [], []]
    for d in sorted(digits_in, reverse=False):
        residues[d % 3].append(d)

    #  Determine how many digits of residue classes 1 and 2 to drop
    gbl_residue = (len(residues[1]) + 2 * len(residues[2])) % 3
    skip = [0, 0, 0]
    if 0 < gbl_residue:
        if 1 <= len(residues[gbl_residue]):
            skip[gbl_residue] = 1
        elif 2 <= len(residues[3 - gbl_residue]):
            skip[3 - gbl_residue] = 2
        else:
            return 0

    #  Make list of output digits from non-dropped digits in residue classes
    digits_out = sorted(residues[0] + residues[1][skip[1]:] + residues[2][skip[2]:], reverse=True)

    #  Concatenate digits and return result
    return reduce(lambda x, y: 10 * x + y, digits_out, 0)
