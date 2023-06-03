'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.oasys.net/posts/google-foobar-programming-challenge"


def solution(l):
    # sorts semver versions by major/minor/integer
    l.sort(key=lambda val: [int(section) for section in val.split(".")])
    return l

