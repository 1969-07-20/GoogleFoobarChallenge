'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://blog.ishandeveloper.com/foobar-2020"


def substring_check(length, sub_str):
    for i in range(0, length-1):
        if(sub_str[i] == sub_str[i+1]):
            if(i == length-2):
                return length
            else:
                continue
        else:
            return 1

def solution(s):
    parts = 1   #Initially, Let's just assume that cake can be divided into just one piece

    for i in range(1, len(s)):
        sub_str = []
        if(len(s) % i == 0):
            for j in range(0, len(s), i):
                sub_str.append(s[j:j+i])
            parts = substring_check(len(sub_str), sub_str)
            if(parts != 1):
                return parts
    return parts
