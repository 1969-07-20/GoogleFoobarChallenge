# -*- coding: utf-8 -*-

'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/douglasbolden/Braille-Translation/blob/main/main.py"


"""
This application is a take on a Braille translator that involves the translation of letters, and spaces only, which
is part of the google challenge:

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never
bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating
her space station. You figure printing out Braille signs will help them, and – since you’ll be promoting efficiency at
the same time – increase your chances of a promotion. Braille is a writing system used to read by touch instead of by
sight. Each character is composed of 6 dots in a 2×3 grid, where each dot can either be a bump or be flat (no bump).
You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda’s
command can feel the bumps on the signs and “read” the text with their touch. The special printer which can print the
bumps onto the signs expects the dots in the following order:

---
1 4
2 5
3 6
---

So given the plain text word “code”, you get the Braille dots:

-----------
11 10 11 10
00 01 01 01
00 10 00 00
-----------

Write a function where 1 represents a bump and 0 represents no bump. Put together, “code” becomes the output string:
“100100101010100110100010”.

Write a function answer(plaintext) that takes a string parameter and returns a string of 1’s and 0’s representing
the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters,
handle capital letters by adding a Braille capitalization mark before that character, and use a blank character
(000000) for spaces. All signs on the space station are less than fifty characters long and use only letters
and spaces.
"""

# BrailleTranslation defines a function that will accept a parameter, "word," and output formatted Braille.


def BrailleTranslation(word):
    # rend is a placeholder that will clear itself each time the function is called.
    rend = ""
    # for loop checks each letter of the "word" parameter that was passed from main.
    for a in word:
        # checks for uppercase letters, and if it is an uppercase letter, adds "000001" to rend.
        if a.isupper():
            rend += '000001'
        # checks for the displayed letter, and if it is found, adds the specified code to rend.
        if a == 'a' or a == 'A':
            rend += '100000'
        if a == 'b' or a == 'B':
            rend += '110000'
        if a == 'c' or a == 'C':
            rend += '100100'
        if a == 'd' or a == 'D':
            rend += '100110'
        if a == 'e' or a == 'E':
            rend += '100010'
        if a == 'f' or a == 'F':
            rend += '110100'
        if a == 'g' or a == 'G':
            rend += '110110'
        if a == 'h' or a == 'H':
            rend += '110010'
        if a == 'i' or a == 'I':
            rend += '010100'
        if a == 'j' or a == 'J':
            rend += '010110'
        if a == 'k' or a == 'K':
            rend += '101000'
        if a == 'l' or a == 'L':
            rend += '111000'
        if a == 'm' or a == 'M':
            rend += '101100'
        if a == 'n' or a == 'N':
            rend += '101110'
        if a == 'o' or a == 'O':
            rend += '101010'
        if a == 'p' or a == 'P':
            rend += '111100'
        if a == 'q' or a == 'Q':
            rend += '111110'
        if a == 'r' or a == 'R':
            rend += '111010'
        if a == 's' or a == 'S':
            rend += '011100'
        if a == 't' or a == 'T':
            rend += '011110'
        if a == 'u' or a == 'U':
            rend += '101001'
        if a == 'v' or a == 'V':
            rend += '111001'
        if a == 'w' or a == 'W':
            rend += '010111'
        if a == 'x' or a == 'X':
            rend += '101101'
        if a == 'y' or a == 'Y':
            rend += '101111'
        if a == 'z' or a == 'Z':
            rend += '101011'
        if a == ' ':
            rend += '000000'
    # prints the final rend after the for loop ends.
    return(rend)
