'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Li-MingQing/googleFooBar-FindTheAccessCodes/blob/main/solution.py"


def solution(l):
    # Your code here
    # Time complexity is O(n^2)
    res = 0
    for num in range(1,len(l)-1):
        left = l[:num]
        right = l[num+1:]
        leftNum = 0
        rightNum = 0
        for nums in left:
            if l[num] % nums == 0:
                leftNum +=1
            else:
                continue
        for nums in right:
            if nums % l[num] == 0:
                rightNum += 1
            else:
                continue
        res += leftNum*rightNum
    return res
