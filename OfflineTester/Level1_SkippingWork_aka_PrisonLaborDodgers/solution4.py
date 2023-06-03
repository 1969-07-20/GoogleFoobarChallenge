'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/72351618/google-foo-bar-hiring-challenge-skipping-work (Turhan Ergene)"


#  Mod:
#  - Return the single element not wrapped in a list


def solution(x, y):
    list_difference1 = [item for item in x if item not in y]
    list_difference2 = [item for item in y if item not in x]

    list_difference = list_difference2 + list_difference1

    return list_difference[0]
