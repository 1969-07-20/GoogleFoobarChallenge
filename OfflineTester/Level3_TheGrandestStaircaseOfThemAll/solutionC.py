'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/oneshan/foobar/blob/master/the_grandest_staircase_of_them_all/solution.py"


"""
The problem can be transfered to Knapsack problem:

1. there are n-1 steps (not n, because we need at least 2 steps)
2. j bricks is needed to build the j-th steps.
3. for each step, we decide whether to build or not to build it

dp[i][j] = the combination of using i bricks to build 1~j steps
dp[i][j] = dp[i][j-1] (not build) + dp[i-j][j-1] (build)
"""


def answer(n):
    dp = [[0] * n for _ in range(n + 1)]
    dp[0][0] = dp[1][1] = dp[2][2] = 1

    for j in range(1, n):
        for i in range(n + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j - 1]

    return dp[-1][-1]
