'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gitlab.com/DevAlone/google_foobar_solutions/-/blob/master/level%201/Prison%20Labor%20Dodgers/main.py"


def answer(x, y):
    # first should be smaller
    x, y = (x, y) if len(x) < len(y) else (y, x)

    ids_set = set(x)

    for item in y:
        if item not in ids_set:
            return item
