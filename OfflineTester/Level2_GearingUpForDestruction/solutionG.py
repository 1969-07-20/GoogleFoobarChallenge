'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/40465866/google-foobar-gearing-up-for-destruction/45626410#45626410 (Debora Dangelo Reina de Araujo)"


from fractions import Fraction

def solution(pegs):
    A, B = make_matrices(pegs)

    sizes = solve_linear_system(A, B)

    for s in sizes:
        if s < 1:
            return [-1, -1]

    return [sizes[0].numerator, sizes[0].denominator]


def make_matrices(pegs):
    tam = len(pegs)

    # make it easier to access specific positions
    A = [[] * (tam)] * (tam)
    B = list(range(tam))

    B[0] = Fraction(pegs[1] - pegs[0])

    # Example for len(pegs) == 3
    # r_0 + r_1 = p_1 - p_0
    # r_1 + r_2 = p_2 - p_1
    # r_1 - 2*r_2 = 0
    # So:
    # A = [[1, 1, 0], [0, 1, 1], [1, 0, -2]]
    # B = [pegs[1] - pegs[0], pegs[2] - pegs[1], 0]

    for i in range(0, tam-1):
        A[i] = [Fraction(0)] * (tam)
        A[i][i] = Fraction(1)
        A[i][i+1] = Fraction(1)
        B[i] = Fraction(pegs[i+1] - pegs[i])

    A[-1] = [Fraction(0)] * (tam)
    A[-1][0] = Fraction(1)
    A[-1][-1] = Fraction(-2)
    B[-1] = Fraction(0)

    return A, B


def solve_linear_system(A, B):
    for i in range(len(A)):

        # let's turn the diagonal equals to 1
        B[i] = B[i] / A[i][i]
        A[i] = multiply_row_by_number(A[i], Fraction(1)/A[i][i])

        # now let's make all values on the column i be zero, except the cell (i, i), that must be 1
        for k in range(len(A)):
            if k == i:
                continue

            B[k] = B[k] - A[k][i] * B[i]
            A[k] = difference_of_lines(A[k], multiply_row_by_number(A[i], A[k][i]))

    return B


def multiply_row_by_number(row, number):
    aux = []

    for r in row:
        aux.append(r*number)

    return aux


def difference_of_lines(line1, line2):
    if (len(line1) != len(line2)):
        return -1

    aux = list(range(len(line1)))

    for i in range(len(line1)):
        aux[i] = line1[i] - line2[i]

    return aux
