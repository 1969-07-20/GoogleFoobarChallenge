'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/povstenko/braille-translation/blob/main/solution.py"


#  Mod:
#  - removed unicode logic


def solution(s):
    res = ""
    for letter in s:
        if letter.isnumeric():
            res += numberic_code
            res += codes[letter]
        if letter.isupper():
            res += upper_code
            res += codes[letter.lower()]
        else:
            res += codes[letter]
    return res

upper_code = '000001'
numeric_code = '001111'
codes = {
    '0': '010110',
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '110010',
    '9': '010100',
    ' ': '000000',
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    ',': '010000',
    '.': '010011',
    '-': '010010',
    '?': '011001',
    '_': '001001',
    '!': '011010'
}
