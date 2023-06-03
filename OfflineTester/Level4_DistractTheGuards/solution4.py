'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ken-power/Foobar_Challenge/blob/main/Level_4/7_DistractTheTrainers/solution.py"


import unittest


def is_power_of_two(n):
    """
    Determine if a given number is a power of 2.

    :param n: an integer
    :return: True if the given integer is a power of 2, otherwise return False
    """

    # Every power of 2 has exactly 1 bit set to 1 (the bit in that number's log base-2 index). So when
    # subtracting 1 from it, that bit flips to 0 and all preceding bits flip to 1. That makes
    # these 2 numbers the inverse of each other so when AND-ing them, we will get 0 as the result.
    #
    #     https://stackoverflow.com/questions/57025836/how-to-check-if-a-given-number-is-a-power-of-two
    return (n & (n - 1) == 0) and n != 0


def gcd(a, b):
    """
    Find the greatest common divisor of two numbers. This implementation uses Euclid's algorithm.

    Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two integers, the
    largest number that divides them both without a remainder. It is named after the ancient Greek mathematician Euclid,
    who first described it in his Elements (c. 300 BC).
    https://en.wikipedia.org/wiki/Euclidean_algorithm

    function gcd(a, b)
        while b != 0
            t := b
            b := a mod b
            a := t
        return a

    See also: https://www.geeksforgeeks.org/gcd-in-python/

    :param a: the first number
    :param b: the second number
    :return: the greatest common denominator of the two numbers
    """
    while b:
        a, b = b, a % b

    return a


def results_in_infinite_loop(banana_count_a, banana_count_b):
    """
    Knowing we must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb
    wrestling loop, this function determines if a specific pair of trainers will enter into an infinite loop.

    :param banana_count_a: the amount of bananas held by trainer a
    :param banana_count_b: the amount of bananas held by trainer b
    :return: True if the two trainers will enter an infinite loop based on their banana count, otherwise return False
    """
    numerator = banana_count_a + banana_count_b
    denominator = gcd(banana_count_a, banana_count_b)
    result = numerator // denominator

    # the wrestling match will enter an infinite loop if result is NOT a power of 2
    return not (is_power_of_two(result))


def create_wrestling_tournament(banana_list):
    """
    Create a graph of the wrestling matches.

    :param banana_list: specifies how many bananas each trainer has
    :return: a graph representing the simultaneous wrestling matches
    """
    tournament_graph = {i: [] for i in range(len(banana_list))}

    for i in range(len(banana_list)):
        for j in range(i, len(banana_list)):
            if i != j and results_in_infinite_loop(banana_list[i], banana_list[j]):
                tournament_graph[i].append(j)
                tournament_graph[j].append(i)

    return tournament_graph


def graph_comparator(graph):
    """
    Compare the graph elements by the length of each of their nodes.
    """
    return lambda x: len(graph[x])


def distract_the_trainers(graph):
    """
    Pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop.

    We don't pair off trainers with the same number of bananas (if we do, their game will end and they will go back to
    work). We know enough trainer psychology to know that the one who has more bananas always gets over-confident and
    loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both
    of them have the same number of bananas. Once that happens, both of them will lose interest and go back to
    supervising the bunny workers, and you don't want THAT to happen!

    The following proved useful and interesting for this implementation:

    References:
    Micali, S. and Vazirani, V.V., 1980, October. "An O (v| v| c| E|) algorithm for finding maximum matching in general
    graphs". In 21st Annual Symposium on Foundations of Computer Science (SFCS 1980) (pp. 17-27). IEEE.
    Wikipedia. Blossom Algorithm. https://en.wikipedia.org/wiki/Blossom_algorithm
    Wolfram. Blossom Algorithm. https://mathworld.wolfram.com/BlossomAlgorithm.html

    :param graph: a graph
    :return: the number of trainers that have gone into an infinite thumb wrestling loop and are now distracted
    """
    distracted_trainers = 0
    remaining_nodes = len(graph)

    while len(graph) > 1 and remaining_nodes >= 1:
        # Find the first min-length path in the graph. Note, there might be multiple paths of the same shortest length.
        min_length_path = min(graph, key=graph_comparator(graph))

        if (len(graph[min_length_path])) < 1:
            del graph[min_length_path]
        else:
            matched_pair = [len(graph[graph[min_length_path][0]]) + 1, 1]

            for node in graph[min_length_path]:
                if len(graph[node]) < matched_pair[0]:
                    matched_pair = [len(graph[node]), node]

                for i in range(len(graph[node])):
                    if graph[node][i] == min_length_path:
                        # We don't pair off trainers with the same number of bananas
                        del graph[node][i]
                        break

            for node in graph[matched_pair[1]]:
                for i in range(len(graph[node])):
                    if graph[node][i] == matched_pair[1]:
                        # We don't pair off trainers with the same number of bananas
                        del graph[node][i]
                        break

            del graph[min_length_path]
            del graph[matched_pair[1]]
            distracted_trainers += 2

        if len(graph) > 1:
            remaining_nodes = len(graph)

    return distracted_trainers


def solution(banana_list):
    """
    A function to pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb
    wrestling loop! The number of trainers will be at least 1 and not more than 100, and the number of bananas each
    trainer starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile
    a LOT of bananas.

    :param banana_list: a list of positive integers depicting the amount of bananas each trainer starts with;
                        Element i of the list will be the number of bananas that trainer i (counting from 0) starts with
    :return: the fewest possible number of bunny trainers that will be left to watch the workers; returns None if any
             of the noted preconditions are violated
    """
    # First, let's check the preconditions that are specified in the problem description
    num_trainers = len(banana_list)

    # The number of trainers will be at least 1 and not more than 100
    if num_trainers < 1 or num_trainers > 100:
        return None

    if num_trainers == 2 and banana_list[0] == banana_list[1]:
        return num_trainers

    # the number of bananas each trainer starts with must be a positive
    # integer no more than 1073741823 (i.e. 2^30 -1)
    max_bananas_per_trainer_at_start = pow(2, 30) - 1

    # If any trainer has more than the allowed starting number of bananas then we won't start a tournament
    for banana_count in banana_list:
        if banana_count > max_bananas_per_trainer_at_start:
            return None

    # if the preconditions are satisfied, we can proceed with figuring out the tournament graph,
    # number of distracted trainers, and remaining trainers
    tournament_graph = create_wrestling_tournament(banana_list)
    distracted_trainers = distract_the_trainers(tournament_graph)
    remaining_trainers = len(banana_list) - distracted_trainers

    return remaining_trainers
