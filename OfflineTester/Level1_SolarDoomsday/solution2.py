'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://livecodestream.dev/challenge/solar-doomsday/?utm_content=expand_article"


def solution(area):
    res = []
    while area > 0:
        biggest_square_side = int(area ** 0.5)
        biggest_square_area = biggest_square_side ** 2
        area -= biggest_square_area
        res.append(biggest_square_area)

    return res
