'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/71058916/foobar-test-case-failing-on-my-solution-on-decrypting-input (Pepsi Joe)"


def solution(x):
    alph = "abcdefghijklmnopqrstuvwxyz"
    response = ""
    
    decryptDic = {c : c_prime for c, c_prime in zip(alph, alph[::-1])}
    
    for char in  x:
        if char == char.upper() or char not in decryptDic:
            response += char    
        else:
            response += (decryptDic.get(char))

    return response
