'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level4_FreeTheBunnyWorkers/freeTheBunnyWorkers.py"


'''
The code in this file computes solutions to the Free the Bunny Workers
challenge.  The function solution(num_bunnies, num_required) is called with
tow integer arguments:
- 'num_bunnies' is the total number of bunnies with keys
- 'num_required' is the minimum number of bunnies required to open the doors.
The function returns a list of lists.  There is one list for each bunny and
each list has the numbers of the keys distributed to that bunny.

Together, two concepts form the foundation to this solution to the Free the
Bunny Workers challenge.  The first concept is that a separate lock is created
for each combination of bunnies which excludes (num_required-1) bunnies.  A copy
of the key for that lock gets distributed to each of the bunnies which are not
excluded from that lock.

The second concept is that since (num_required - 1) bunnies are excluded from
opening any given lock, and all possible combinations of (num_required - 1)
bunnies are excluded from one and only one lock, then any combination of
num_required bunnies is guaranteed to have at least one key for all locks.

The implementation of the above solution to the problem first finds all possible
combination of bunnies which exclude (num_required-1) bunnies.  Each combination
is recorded as a string of binary digits where each digit corresponds to a bunny
and the digit for a bunny will be '0' if that bunny is excluded from opening
that lock and '1' if it is not.  The resulting list of strings are sorted in
reverse order.  This ensures that when the keys are distributed in the last step,
they are distributed in lexicographic order.

Finally, the keys for each lock are distributed to the eligible bunnies.  The
keys get distributed in a manner which meets the lexicographic distribution
constraint when
(a) the number assigned to a lock is the index of the string in the sorted list
(b) the index of the binary digit in the string is the bunny which receives
    a key based on whether that digit is a '1' or a '0'.
'''

def solution(num_bunnies, num_required):

    #  Handle the null case
    if 0 == num_required:
        return [ [] for b in range(num_bunnies) ]

    #  Create format string for label
    fmt_str = '{:0' + str(num_bunnies) + 'b}'

    #  Loop over all possible combinations of m out of n bunnies (of whih there
    #  are two raised to the power of num_bunnies), and record those
    #  combinations which exclude (num_bunnies - num_required bunnies).
    locks = []

    for idx in range(2**num_bunnies):
        label = fmt_str.format(idx)

        #  If this combination has the right number of bunnies make a lock for it.
        if label.count('1') == (num_bunnies - (num_required - 1)):
            locks.append(label)

    #  Sort the combinations so that the locks that get created will be
    #  distributed in lexicographic order.
    locks.sort(reverse=True)

    #  Create zero length lists to hold each bunny's list of keys
    keys = [[] for b in range(num_bunnies)]

    #  Create locks for each combination of bunnies
    for idx_lock in range(len(locks)):
        dist_list = list(locks[idx_lock])

        #  Distribute keys to each bunny in this lock's particular combination
        #  of bunnies
        for idx_bunny in range(num_bunnies):
            x = dist_list[idx_bunny]

            if '1' == x:
                keys[idx_bunny].append(idx_lock)

    return keys
