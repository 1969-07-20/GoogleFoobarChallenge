'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/fmbxnary/fuel-injection-perfection/blob/main/solution.py"


def priority(n):
    count = 0
    while (n % 2 == 0):
        count += 1
        n = n // 2
    return count


def solution(n):
    n = int(n)
    count = 0
    while (n != 1):
        if (n % 2 == 0):
            n //= 2
        elif (priority(n + 1) > priority(n - 1) and n > 3):
            n = n + 1
        else:
            n = n - 1
        count += 1
    return count
