'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/42378334/google-foo-bar-challenge-help-minion-salutes (shivangg)"


#  Mod:
#  - Change "is" to "==" in comparison with a literal.


def answer(s):
    # your code herecat 
    multiplier = 0
    salute = 0
    for x in range(len(s)):
        if s[x] == '<':
            multiplier += 1

    for x in range(len(s)):
        if s[x] == '>':
            salute += multiplier
        elif s[x] == '<':
            multiplier -= 1

    ans = salute * 2

    return ans
