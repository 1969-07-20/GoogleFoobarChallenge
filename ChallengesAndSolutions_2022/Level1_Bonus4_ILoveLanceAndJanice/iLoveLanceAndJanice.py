"""  This file computes solutions to the "I Love Lance & Janice" challenge.

The strategy implemented in this solution is to create a dictionary which
serves as a mapping from cipher text to plain text.  This dictionary is then
referenced when constructing the plain text from the cipher text.

Note:  This would have been much more succinct in Python 3 using the
maketrans() and translate() methods of strings.
"""


def solution(s):
    """Function solution(s) computes solutions to the "I Love Lance & Janice"
    challenge.  Given sting s, solution() returns a string in which the lower
    case characters of s are replaced according to the mapping [a-z] --> [z-a].
    """

    #  Create the mapping from cipher text to plain text
    p_chars = 'abcdefghijklmnopqrstuvwxyz'
    c_chars = p_chars[::-1]

    decoder_ring = {}

    for [p_char, c_char] in zip(p_chars, c_chars):
        decoder_ring[c_char] = p_char

    #  Perform the translation of cipher text to plain text
    result = ''
    for c in s:
        if c in decoder_ring:
            result += decoder_ring[c]
        else:
            result += c

    return result
