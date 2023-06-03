'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ken-power/Foobar_Challenge/blob/main/Level_4/8_RunningWithBunnies/solution.py"


import itertools
import unittest


def all_pairs_shortest_paths(graph):
    """
    This implementation uses the Floyd-Warshall algorithm to find the shortest path for all (row, col) pairs in the
    given graph. The Floyd-Warshall algorithm is a good choice for computing paths between all pairs of vertices in
    dense graphs, in which most or all pairs of vertices are connected by edges.
    https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm

    :param graph: a dense graph represented as a square matrix
    """
    n = len(graph)

    for k in range(n):  # step
        for i in range(n):  # row
            for j in range(n):  # column

                # If an edge is found to reduce distance, update the shortest paths
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


def path(bunnies):
    """
    Given a list of bunnies, return a path to pick up the bunnies.

    :param bunnies: a list of bunnies
    :return: a path that visits the list of bunnies
    """
    bunnies = [0] + bunnies + [-1]
    path_to_bunnies = list()

    for i in range(1, len(bunnies)):
        path_to_bunnies.append((bunnies[i - 1], bunnies[i]))

    return path_to_bunnies


def solution(times, time_limit):
    """
    Calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead
    before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies
    with the lowest worker IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by worker ID,
    with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at
    most 999.

    :param times: a matrix
    :param time_limit: the time limit
    :return: the ids of the rescued bunnies
    """
    max_time_limit = 999
    if time_limit < 0 or time_limit > max_time_limit:  # time_limit is a non-negative integer that is at most 999
        return []

    all_pairs_shortest_paths(times)

    n = len(times)  # number of rows
    bunny_count = n - 2  # first row is "Start", last row is "Bulkhead"
    rescued_bunnies = []

    for bunny in range(n):
        if times[bunny][bunny] < 0:  # check the diagonal
            rescued_bunnies = [bunny for bunny in range(bunny_count)]
            return rescued_bunnies

    for bunny in reversed(range(bunny_count + 1)):

        for bunnies in itertools.permutations(range(1, bunny_count + 1), r=bunny):
            total_time = 0

            path_to_bunnies = path(list(bunnies))

            for start_time, end_time in path_to_bunnies:
                total_time += times[start_time][end_time]

            if total_time <= time_limit:
                rescued_bunnies = sorted(list(bunny - 1 for bunny in bunnies))
                return rescued_bunnies

    return rescued_bunnies
