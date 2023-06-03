'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://codereview.stackexchange.com/questions/149440/google-foobar-xor-checksum-challenge (301_Moved_Permanently)"


#  Mod:
#  - Changed xrange to range
#  - Added import of reduce when running under Python
#  - Added import of operator


import operator

import sys
if 3 == sys.version_info[0]:
    from functools import reduce 


def xor_in_range(a, b):
    return reduce(operator.xor, range(a, b), 0)


def answer(start, length):
    return reduce(
        operator.xor,
        (xor_in_range(begin, begin+length-i)
          for i, begin in enumerate(range(start, start + length * length, length))),
        0)
