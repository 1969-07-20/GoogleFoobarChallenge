'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rudisimo/google-foobar/blob/master/solutions/elevator_maintenance/solution.py"


#  Mod:
#  - if running under Python 3, have to create a list from the result of the map().


import sys

def answer(l):
    # sort using simple semver comparison function
    if 3 == sys.version_info[0]:
        l.sort(key=lambda v: list(map(int, v.split('.'))))
    else:
        l.sort(key=lambda v: map(int, v.split('.')))
    # return sorted list
    return l
