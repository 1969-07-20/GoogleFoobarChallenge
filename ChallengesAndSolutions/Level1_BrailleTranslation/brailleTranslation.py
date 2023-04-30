"""  This file computes solutions to the "Braille Translation" challenge.

The strategy implemented in this solution is to create a dictionary which
serves as a mapping from plaintext to Braille.  This dictionary is then
referenced when constructing the Braille string text from the plain text.

Creating the plaintext to Braille mapping is complicated by the fact that the
problem statement does not explicitly give the Braille encoding for each letter
of the alphabet.  The problem statement does give the Braille for the famous
sentence "The quick brown fox..." This sentence is famous because every letter
of the alphabet appears at least once. This solution uses this sentence and its
Braille equivalent to construct a dictionary which provides the mapping from
plain text to Braille used later.
"""


def solution(plaintext):
    """Function solution(plaintext) computes solutions to the "Braille
    Translation" challenge.  Given sting plaintext, solution() returns a string
    in which encodes how the Braille printer should print a sign which conveys
    that message in Braille."""

    #  Create a mapping from plaintext to Braille using a known (plaintext,
    #  Braille) pair of texts which uses all letters in the alphabet.
    encoder_ring = {}

    p_text = 'The quick brown fox jumps over the lazy dog'
    c_text = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'

    idx = 0

    for p in p_text:
        if p.isupper():
            encoder_ring['CAP'] = c_text[idx:idx+6]
            idx = idx + 6

            encoder_ring[p.lower()] = c_text[idx:idx+6]
            idx = idx + 6
        else:
            encoder_ring[p] = c_text[idx:idx+6]
            idx = idx + 6

    #  Use mapping from plaintext to Braille to create the Braille string
    result = ''
    for p in plaintext:
        if p.isupper():
            result += encoder_ring['CAP']
            result += encoder_ring[p.lower()]
        else:
            result += encoder_ring[p]

    #  Return result
    return result
