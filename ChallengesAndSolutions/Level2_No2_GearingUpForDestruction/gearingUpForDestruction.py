"""  Solution to 'Gearing Up for Destruction' puzzle.

Description of algorithm:
    Observation:  In this type of gear arrangement, the distance traveled by
    a fixed point on the rim is the same for all gears.  The number of rotations
    of any given gear is the distance traveled divided by the circumference of
    the the gear, which is proportional to the gear's radius.  Therefore, in
    order for the last gear to rotate at twice the rate of the first gear, the
    radius of the first gear needs to be twice that of the last.  The radii of
    the gears in between do not matter except to the extent they need to touch
    their neighbors in order to engage them.  (And the gears cannot be of a
    size so that causes them to hit obstructions.)

    This also means that the size of each gear is fully determined by the radius
    of the first gear.  The solution computes the radius of the last gear as a
    function of the radius of the first and then seeks a solution in which the
    radius of the last gear is one half that of the first.

    Let r(n) and r(n-1) be the radii of two adjacent gears located at pegs n-1
    and n, and let g(n) be the gap between their centers.  For the gears to make
    contact, the sum of the radii need to add up to g(n), i.e. g(n) = r(n) +
    r(n-1).  This allows us to set up a recursion relation that expresses the
    size of the gear at peg n in terms of the radius of the gear at peg n-1:
    r(n) = g(n) - r(n-1).

    Given the peg positions, we can find the values of the gaps g(i) and applying
    the recursion we can express the radius of the last gear in terms of the
    radius of the first.  Applying the recursion relation to the pegs at n and
    n - 1 gives:

    r(n-1) = g(n-1) - r(n-2)

    and

    r(n) = g(n) - r(n-1)

    Substituting the first into the second gives:

    r(n) = g(n) - (g(n-1) - r(n-2) = g(n) - g(n-1) + r(n-2)

    From this we can see that once the recursion reaches the first gear (r(0))
    it's form will be:

    r(N) = c1*r(0) + c0

    for some constants c1 and c0.  Furthermore, c1 takes on the value of 1 or
    -1.

    From above we know that the radius of the first gear must be twice that of
    the last, i.e. r(0) = 2*r(N), where N is the index of the last gear.
    Substituting for r(N) gives r(0) = 2*(c1*r(0) + c0).  Solving for the
    radius of the first gear, r(0), gives:

    r(0) = c0 / (1 - 2*c1)

    This recursion relation allows us to find the radius of the last gear in
    terms of the radius of the first.  We just need to apply the recursion
    relation to find the constants c0 and c1.

Time and space complexity of the solution:
    To compute a candidate size of the first gear, the solution makes a single
    pass through the list of N pegs, evaluating the recursion relation for each
    at each peg/gear.  Each evaluation takes O(1) work.  To do this, O(1)
    storage is required beyond the O(N) storage required of the input.
    Identifying the candidate solution requires O(N) work and O(N) storage.

    To determine the feasibility of the candidate solution another pass is made
    through the list evaluating the size of each intermediate gear and checking
    if each gear satisfies its constraints.  O(1) work is performed for each
    gear giving O(N) time complexity for the verification process.  Verification
    requires O(1) storage beyond that of the input.

    Beyond these two steps, O(1) work and storage are required.  Overall, the
    solution requires O(N) time and O(N) storage.

Assumptions/restrictions:
    Assume there are no obstructions before the first peg or beyond the last peg
    that can constrain the answer.

This solution is completely of my own conception and execution.
"""

from fractions import gcd


def solution(pegs):
    """Compute size of first gear, expressed as an rational number, such that
    rotations of first gear is one half that of last for the given arrangement
    of pegs."""

    #  Process the peg locations in order.  Iteratively find the radius of the
    #  last gear as a function of the radius of the gear being considered.
    c1 = 1
    c0 = 0
    pos_lst = pegs[0]
    for pos_cur in pegs[1:]:
        gap = pos_cur - pos_lst

        c0 = gap - c0
        c1 = -c1

        pos_lst = pos_cur


    #  Calculate the radius of the first gear
    r0_numer = 2 * c0
    r0_denom = 1 - 2 * c1


    #  Reduce fraction
    greatest_common_factor = gcd(r0_numer, r0_denom)

    r0_numer /= greatest_common_factor
    r0_denom /= greatest_common_factor


    #  Using the calculated value of the first gear, calculate the sizes of the
    #  rest.  Return [-1,-1] if any gear is infeasible, i.e. the size is not in
    #  [1,gap-1]
    peg_lst = pegs[0]
    radius_lst = r0_numer / r0_denom

    gap = pegs[1] - pegs[0]
    if (radius_lst < 1) or (radius_lst > (gap - 1)):
        return [-1, -1]

    for peg_nxt in pegs[1:]:
        gap = peg_nxt - peg_lst

        radius_nxt = gap - radius_lst

        if (radius_nxt < 1) or (radius_nxt > (gap - 1)):
            return [-1, -1]

        peg_lst = peg_nxt
        radius_lst = radius_nxt


    #  Candidate solution passes viability test, return it
    return [r0_numer, r0_denom]


# print(solution([4, 30, 50]))
# #  Output: 12,1

# print(solution([4, 17, 50]))
# #  Output: -1,-1
