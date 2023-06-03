'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://blog.everythingdev.com/2020/12/google-foobar-please-pass-coded-messages.html"


def solution(l):
    lLen = len(l)
    max = 1 << lLen
    l.sort(reverse=True)
    maxAttempt = 0
    for mask in reversed(range(max)):
        attempt = ""
        for index in range(mask.bit_length()):
            attempt += str(l[index]) if (mask >> index) & 1 == 1 else ''
        if attempt == '':
            attempt = 0
        attempt = int(attempt)
        if attempt % 3 == 0:
            if attempt > maxAttempt:
                maxAttempt = attempt

    return maxAttempt
