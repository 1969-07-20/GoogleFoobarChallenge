'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/52654530/programming-challenge-how-does-this-algorithm-tied-to-number-theory-work (franz)"


def deduct(bricks_left, prev_step, memo={}):
    memo_name = "%s,%s" % (bricks_left, prev_step)
    if memo_name in memo:
        return memo[memo_name]
    if bricks_left == 0: return 1
    if bricks_left != 0 and prev_step <= 1: return 0

    count = 0
    for first_step in range(bricks_left, 0, -1):
        if first_step >= prev_step: continue
        next_step = bricks_left - first_step
        count += deduct(next_step, first_step, memo)
    memo[memo_name] = count
    return count


def solution(n):
    return deduct(n, n)
