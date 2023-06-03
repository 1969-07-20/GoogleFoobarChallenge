'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ehraazatif/the_cake_is_not_a_lie/blob/main/src/solution.py"


#  Mod:
#  - replace floating point division with integer division to ensure an integer is returned

def solution(s):
    valid = True
    for slice_length in range(1, len(s)):
        if len(s) % slice_length == 0:
            for i in range(0, len(s), slice_length):
                if s[:slice_length] != s[i:i+slice_length]:
                    valid = False
                    break
                
            if valid:
                return len(s)//slice_length
            else:
                valid = True
            
    return 1            
