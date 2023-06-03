'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/AsafTzarfati/Foobar__I_love_lance_janice/blob/main/I_love_lance_janice.py"


def solution(secret):
    cipher_dict = {
                    "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s",
                    "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k",
                    "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c",
                    "y": "b", "z": "a"
                   }
    decrypted = list()
    for char in secret:
        if char in cipher_dict:
            decrypted.append(cipher_dict[char])
        else:
            decrypted.append(char)
    decrypted = ''.join(decrypted)

    return decrypted
