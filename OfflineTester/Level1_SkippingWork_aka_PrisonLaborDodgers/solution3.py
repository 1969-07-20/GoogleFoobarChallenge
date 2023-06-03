'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/66281099/python-test-cases-fails-in-google-foobar-challenge (Amir Khan)"


def solution(x, y):
    set1 = set(x)
    set2 = set(y)
    unique = list(set1 ^ set2)
    return unique[0]
