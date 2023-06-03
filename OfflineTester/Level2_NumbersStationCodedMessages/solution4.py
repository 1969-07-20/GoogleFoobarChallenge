'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://matthosch.hashnode.dev/completing-the-google-foobar-challenge-part-2-ckcviwnf200sk7os17oopap5h"


def optimized_answer(l, t):
    # Store key values in dictionary with sum:index
    dict = {}
    # Initialize with 0: -1 in case sublist starts from index 0
    dict[0] = -1
    sum = 0
    # traverse the given list
    for i in range(len(l)):
        # sum of elements so far
        sum += l[i]
        # If the sum hasn't been recorded, add to dict
        if sum not in dict:
            dict[sum] = i
        # If sum - t exists in dict, we've found a valid solution
        if sum - t in dict:
            # Subtract index of sum - t
            length = i - dict[sum - t]
            return [i - length + 1, i]
    # No valid values found
    return [-1, -1]
