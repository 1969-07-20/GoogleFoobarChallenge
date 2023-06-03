'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ken-power/Foobar_Challenge/blob/main/Level_1/1_LanceAndJanice/solution.py"


import unittest


def solution(s):
    """
    Take in a string and returns the deciphered string.

    :param s: a cipher text string 
    :return: the deciphered string
    """
    if len(s) == 0:
        return ""

    max_supported_size = 1000000    # Arbitrarily limiting input string to 1MB for illustrative purposes

    if len(s) > max_supported_size:
        # print("Try breaking the message into smaller chunks. Max supported message size =", max_supported_size, "bytes")
        return ""

    cipher_text = list(s)
    plain_text = ""

    a = ord('a')    # unicode code for 'a' is 97
    z = ord('z')    # unicode code for 'z' is 122
    alphabet_size = z-a+1     # assuming lowercase alphabet in range 97...122

    for character in cipher_text:

        if ord(character) in range(a, z+1):   # if the unicode equivalent of the character is in the specified range
            character = chr(a + (alphabet_size - (ord(character) - a))-1)    # decode the input character
        elif character not in range(a, z+1):
            character = character
        else:
            character = ' '
        plain_text = plain_text + character

    return str(plain_text)
