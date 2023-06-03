'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://carlosgrande.me/google-challenge-01"


def solution(x):
    # Define a string with the alphabet
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # Reverse the alphabet string
    alpha_reverse = alpha[::-1]
    # Generate a mapped dictionary
    abc_map = dict(zip(alpha, alpha_reverse))
    # Decode de message in a loop
    decode_lst = [abc_map[letter] if letter in alpha else letter for letter in x]
    # Join back the message in a string
    decode_message = ''.join(decode_lst)
    return decode_message
