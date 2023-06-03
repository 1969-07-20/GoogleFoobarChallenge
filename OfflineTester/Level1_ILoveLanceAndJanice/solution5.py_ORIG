'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/franklinvp/foobar/blob/master/foobar2020/solutionProblem20.py"


"""
Oops, it looks like I forgot to save this solution.
Will have to re-do it, but won't be able to test it against the secret
test cases. Fortunately this one is not particularly hard.
"""

decode = {'a':'z',
          'b':'y',
          'c':'x',
          'd':'w',
          'e':'v',
          'f':'u',
          'g':'t',
          'h':'s',
          'i':'r',
          'j':'q',
          'k':'p',
          'l':'o',
          'm':'n',
          'n':'m',
          'o':'l',
          'p':'k',
          'q':'j',
          'r':'i',
          's':'h',
          't':'g',
          'u':'f',
          'v':'e',
          'w':'d',
          'x':'c',
          'y':'b',
          'z':'a',}

def solution(s):
    result = []
    for c in s:
        if c in decode:
            result.append(decode[c])
        else:
            result.append(c)
    return "".join(result)
