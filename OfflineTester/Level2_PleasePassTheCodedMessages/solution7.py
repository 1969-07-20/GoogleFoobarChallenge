'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/52584048/google-foobar-question-please-pass-the-coded-message (Special_octo20)"


from itertools import combinations

def answer(nums):
    nums.sort(reverse = True)
    for i in reversed(range(1, len(nums) + 1)):
        for tup in combinations(nums, i):
            if sum(tup) % 3 == 0: return int(''.join(map(str, tup)))
    return 0
