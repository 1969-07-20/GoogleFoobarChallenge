'''
The function solution(num_bricks) computes the total number of distinct
staircase configurations that can be made from num_bricks bricks.  Each
column of bricks must have a distinct number of bricks.

A constructivist approach could be used to determine the number of distinct
configurations.  However, abstracting the problem opens up another avenue of
attack.  We know the total number of bricks and the fact that each step must
be unique.  This abstracts to the mathematical problem of determining the
number of ways a positive integer N (=num_bricks) can be partitioned into
distinct smaller numbers such that they sum to N.

A recurrence relation for the number of partitions is given by the Pentagonal
Number Theorem.  (https://en.wikipedia.org/wiki/Partition_(number_theory),
https://en.wikipedia.org/wiki/Pentagonal_number_theorem).  The recurrence form
provides the opportunity to use dynamic programming techniques to improve
improve speed.  The recurrence relation can be found at
https://mathworld.wolfram.com/PartitionFunctionQ.html.

The recurrence relation is much faster than the constructivist approach.  One
constructivist approach would determine the number of distinct staircases and
the number of bricks used for increasingly higher staircases until all bricks
were used in one step and sum up the number of bricks.  This would involve
loops nested three deep, two of which are O(n) and one greater than O(n) in
time complexity.
'''

def solution(total_bricks):
    q_state = {}

    s = generate_s(total_bricks)

    return q(total_bricks, s, q_state) - 1

#  Function generate_s(n) generates the s(n) values used in the recurrence
#  relation given on the link to the Mathworld website.
def generate_s(n):
    s = {}

    j = 0
    val = 1
    while True:
        np = round(j * (3 * j + 1) / 2)
        nm = round(j * (3 * j - 1) / 2)

        if np > n and nm > n:
            break

        s[np] = val
        s[nm] = val

        j = j + 1
        val = -val

    return s

#  Function q(n, s, q_state) implements the recurrence relation given on the line
#  to the Mathworld website.  The argument n is the integer for with the number of
#  partitions to be found, s is the pre-computed term in the recurrence relation
#  and q_state is a dictionary which holds previously computed values of q(n)
#  which can be reused in a dynamic programming optimization.
def q(n, s, q_state):
    if (n < 0):
        return 0

    if n in q_state:
        return q_state[n]

    val = s[n] if (n in s) else 0

    k = 1
    sign = 1
    while k * k <= n:
        val = val + 2 * sign * q(n-(k*k), s, q_state)

        k = k + 1
        sign = -sign

    q_state[n] = val

    return val


if __name__ == '__main__':
    print(solution(200))
