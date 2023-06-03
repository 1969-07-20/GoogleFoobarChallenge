'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://codereview.stackexchange.com/questions/200535/finding-the-position-in-a-triangle-for-the-given-challenge (Graham)"

def answer(x, y):
    y_diff = y - 1
    corner = x + y_diff
    id = corner * (corner + 1) // 2
    id -= y_diff
    return str(id)
