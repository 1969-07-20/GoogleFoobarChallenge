'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/povstenko/the-grandest-staircase-of-them-all/blob/main/solution.py"


from functools import reduce

def solution(n):
    cache = {}
    
    def count_stairs(start, left):
        if (start, left) not in cache:
            if left == 0:
                cache[(start, left)] = 1
            elif left <= start:
                cache[(start, left)] = 0
            else:
                cache[(start, left)] = reduce(lambda x, item: x + count_stairs(item, left - item), range(start + 1, left + 1), 0)

        return cache[(start, left)]
    
    return count_stairs(0, n) - 1
