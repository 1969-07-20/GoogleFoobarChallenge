'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://randomds.com/2022/01/28/google-foobar-challenge-level-2-elevator-maintenance"


from distutils.version import LooseVersion
def solution(l):
    #eturn ",".join(sorted(l, key=LooseVersion))
    return sorted(l, key=LooseVersion)
