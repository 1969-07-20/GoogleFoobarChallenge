'''
The function solution(times, time_limit) computes solutions to the Prepare the
Bunnies' Escape problem.  Given 'times' a 2D array with travel times between
bunny locations as well as the entrance and exit, and 'time_limit' the maximum
time allowed, solution() returns the list of bunny IDs of the set of maximum
bunnies that can be carried to the exit during the time limit.

Two aspects to the problem set up are key to the solution.  The first is that
traversing path segments multiple times is allowed.  The second is the fact
that traversing certain segments can add time on the clock.  Because of the
negative times consumed it can be advantageous to include these path segments.
Moreover, the presence of negative times combined with multiple traversals
of path segments being allowed may result in cyclic paths with negative
traversal times.  Because the negative cycles may be traversed multiple times
their presence effective allows infinite time to save the bunnies.

solution() has two phases.  The first phase computes uses the Floyd-Warshall
algorithm to compute the minimum time between all pairs of locations.  These
minimum times between all points are then used in the second phase.  In the
second phase solutions computes the time from the start to the exit of all
for all possible permutations of all subsets of bunnies.  For each permutation
of bunnies the time required to go from the entrance to each bunny (in order)
to the exit is computed.  In this way the maximum size set of bunnies that
can be saved within the time constraint is identified.

The algorithms used have high time complexity.  Finding the minimum time between
all pairs of locations is O(l^3) in the number of locations l.  The number of
subsets of bunnies is O(2^b) in the number of bunnies b.  However, the number of
bunnies is limited to a maximum of 5, hence the time required by solution() will
be acceptable.  The space complexity is dominated by the space required to store
the travel times between all pairs of locations hence is O(l^2).
'''

from itertools import chain, combinations, permutations
from copy import deepcopy


#  Function powerset() computes the power set of the input, i.e. the set of all
#  subsets of the input.  Code taken from
#  https://stackoverflow.com/questions/18035595/powersets-in-python-using-itertools
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


#  Function all_pairs_shortest() implements the Floyd-Warshall algorithm to
#  compute the shortest time between all pairs of nodes (bunnies).  The
#  algorithm handles negative weights (times) and cycles.  See
#  https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm
def all_pairs_shortest(times_in):

    times = deepcopy(times_in)

    for k in range(len(times)):
        for j in range(len(times)):
            for i in range(len(times)):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]

    return times


def solution(times_in, time_limit):

    #  Compute the shortest path between all locations
    times = all_pairs_shortest(times_in)

    #  If there are any negative cycles then essentially infinite time is
    #  available to recue bunnies and therefore all can be rescued
    for i in range(len(times)):
        if times[i][i] < 0:
            return [(idx-1) for idx in range(1, len(times) - 1)]

    #  Initialize dict to hold best candidate during iteration over permutations
#   best = {'perm': [], 'id': '', 'time': times[0][-1]}
    best = {}

    #  Loop over all subsets
    for subset in powerset(range(1, len(times)-1)):
        size = len(subset)

        #  Skip empty set; which was used to initialize 'best'
        if size == 0:
            best = {'perm': [], 'id': '', 'time': times[0][-1]}
            continue

        #  Loop over all permutations of subset
        for perm in permutations(subset):

            time = times[0][perm[0]] + times[perm[-1]][-1]
            for idx_node in range(size-1):
                node0 = perm[idx_node]
                node1 = perm[idx_node+1]

                time += times[node0][node1]

            #  Reject permutation if saving this set of bunnies exceeds the time limit
            if time > time_limit:
                continue

            #  Reject permutation if this set of set of bunnies is smaller than best set so far
            if size < len(best['perm']):
                continue

            #  Compute ID string to use in comparisons
            id_str = ''.join(str(sorted(list(set(perm)))))

            #  Keep if this set is larger than previous sets
            if size > len(best['perm']):
                best = {'perm': perm, 'id': id_str, 'time': time}

            #  Or keep if this set of bunnies if the ID string sorts earlier
            elif id_str < best['id']:
                best = {'perm': perm, 'id': id_str, 'time': time}

    #  Create sorted list of bunny IDs
    bunny_ids = sorted([(idx - 1) for idx in best['perm']])

    return bunny_ids


if __name__ == '__main__':
    print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
    print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
    print(solution([[0, 1, 1, 1, 1], [1, 0, -10, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
    print(solution([[0, 3, 3, 3, 1], [3, 0, 3, 3, 3], [3, 3, 0, 3, 3], [3, 3, 3, 0, 1], [-2, 3, 3, 3, 0]], 3))
