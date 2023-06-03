'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ehraazatif/please_pass_the_coded_messages/blob/main/solution.py"


def solution(L):
    num = 0
    for i in range(0, len(L)):
        num += 2 ** i

    bin_variations = []
    for i in range(num, 0, -1):
        to_add = bin(i)[2:]
        while len(to_add) != len(L):
            to_add = '0' + to_add
        bin_variations.append(to_add)

    L.sort(reverse=True)
    max_num = float('-inf')
    for v in bin_variations:
        s = ""
        for i in range(0, len(L)):
            if v[i] == "1":
                s += str(L[i])
        s = int(s)
        if s > max_num and s % 3 == 0:
            max_num = s

    if max_num == float('-inf'):
        return 0
    else:
        return max_num
