'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/gggauravgandhi/aafa3f09c795e495220090ab7fb6ae80"


# Quiz: Gearing Up for Destruction
# ==========================

# As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

# The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

# Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function answer(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function answer(pegs) should return the list [-1, -1].

# For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and answer(pegs) should return [12, 1].

# The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

# Solution (Thanks to https://gist.github.com/1lann/be45311db1bd8cbbe6650b0a3e9d1977)
# ==========================
from fractions import Fraction

def invert(matrix):
    n = len(matrix)
    inverse = [[Fraction(0) for col in range(n)] for row in range(n)]

    for i in range(n):
        inverse[i][i] = Fraction(1)

    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][i] == 0:
                    return false
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(n):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in range(n):
        a = matrix[i][i]
        if a == 0:
            return false
        for j in range(n):
            inverse[i][j] = inverse[i][j] / a
    return inverse


def answer(pegs):
    if len(pegs) < 2:
        return [-1, -1]

    if len(pegs) == 2:
        x = (Fraction(pegs[1] - pegs[0]) / Fraction(3)) * Fraction(2)
        if (x.numerator < 1) or (x.numerator < x.denominator):
            return [-1, -1]

        return [x.numerator, x.denominator]

    matrix = []
    rowNum = 0
    deltas = []
    for loc in pegs:
        deltas.append(Fraction(pegs[rowNum + 1] - pegs[rowNum]))

        if rowNum == 0:
            row = [Fraction(2), Fraction(1)] + [Fraction(0)] * (len(pegs) - 3)
            matrix.append(row)
        elif rowNum == len(pegs) - 2:
            row = [Fraction(1)] + [Fraction(0)] * (len(pegs) - 3) + [Fraction(1)]
            matrix.append(row)
            break
        else:
            row = [Fraction(0)] * rowNum + [Fraction(1), Fraction(1)] + [Fraction(0)] * (len(pegs) - rowNum - 3)
            matrix.append(row)
        rowNum = rowNum + 1

    inverse = invert(matrix)
    if not(inverse):
        return [-1, -1]

    # Validate all gears
    for i in range(1, len(pegs)-1):
        y = Fraction(0)
        for j in range(len(pegs)-1):
            y = y + inverse[i][j] * deltas[j]
        if (y.numerator < 1) or (y.numerator < y.denominator):
            return [-1, -1]

    x = Fraction(0)
    for i in range(len(pegs)-1):
        x = x + inverse[0][i] * deltas[i]

    x = x * Fraction(2)

    if (x.numerator < 1) or (x.numerator < x.denominator):
        return [-1, -1]

    return [x.numerator, x.denominator]
