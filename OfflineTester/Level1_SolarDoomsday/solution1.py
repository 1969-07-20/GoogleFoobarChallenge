'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level1_SolarDoomsday/solarDoomsday.py"


import math

"""  This file computes solutions to the "Solar Doomsday" challenge.

This pass repeatedly computes the largest integer less than or equal to the
square root of the amount of material currently available to make solar panels.
The square of that integer is subtracted from the material currently available
until no material is left to make additional solar panels.

All material is guaranteed to be used up because a) the input material and sides
of the solar panels made from it are integers and b) the smallest square is 1
which divides evenly into any remaining amount of material after a solar panel
is made.
"""

def solution(area):
    """Function solution(area) computes solutions to the "Solar Doomsday
    challenge.  Given area as an input value this function returns a list of
    largest squares of integer dimension that can be made from the area amount
    of material, sorted from largest to smallest.
    """

    val = int(math.sqrt(area))
    val_sq = val * val

    result = []

    while area > 0:
        if area >= val_sq:
            result.append(val_sq)

            area -= val_sq
        else:
            val = int(math.sqrt(area))

            if val == 0:
                return result

            val_sq = val * val

    return result
