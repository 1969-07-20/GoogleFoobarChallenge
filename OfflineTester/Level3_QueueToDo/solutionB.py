'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ken-power/Foobar_Challenge/blob/main/Level_3/4_QueueToDo/solution.py"


import unittest


def xor_of_sequence(first, last):
    """
    Get the XOR of a sequence of numbers. We can take advantage of the fact that the XOR operation repeats itself for
    sequential numbers.

    :param first: the first number in the sequence
    :param last: the last number in the sequence
    :return: the XOR of the sequence
    """
    if first % 2 == 0:  # if the first number in the sequence is even
        xor_pattern = [last, 1, last + 1, 0]
    else:  # if the first number in the sequence is odd
        xor_pattern = [first, first ^ last, first - 1, (first - 1) ^ last]

    return xor_pattern[(last - first) % 4]  # the XOR pattern repeats every 4 numbers


def solution(start, length):
    """
    A function that returns the same security checksum that the bunny trainers would have after they
    would have checked all the workers through. Fortunately, the workers' orderly nature causes them to always
    line up in numerical order without any gaps.

    :param start: a positive integer representing the ID of the first worker to be checked
    :param length: a positive integer representing the length of the line before the automatic review occurs
    :return: the same security checksum that the bunny trainers would have after they would have checked all
             the workers through
    """
    # All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the checkpoint line
    # will always be at least 1 worker long.
    max_id = 2000000000
    range_boundary = start + length * length

    if range_boundary > max_id or start < 0 or length < 0:
        return None

    security_checksum = 0

    for security_id in range(0, length):  # treat each 'row' as a sequence of numbers
        first = start + (length * security_id)  # the first number in the row / sequence
        last = first + (length - security_id) - 1  # the last number in the row / sequence

        security_checksum ^= xor_of_sequence(first, last)  # update the checksum with the XOR for each row

    return security_checksum
