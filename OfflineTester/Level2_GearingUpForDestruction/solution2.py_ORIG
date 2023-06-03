'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://jasonqsy.github.io/algorithm/2018/01/06/Google-foobar.html"


from fractions import Fraction

def answer(pegs):
    if len(pegs) == 2:
        # it is not a linear system
        x = [Fraction(pegs[1] - pegs[0]) / 3]
    else:
        # solve linear system
        dim = len(pegs) - 1
        A = [[Fraction(0) for _ in range(dim)] for _ in range(dim)]
        b = [Fraction(0) for _ in range(dim)]
        for i in range(dim):
            n = (i + 1) % dim
            b[i] = Fraction(pegs[i + 1] - pegs[i])
            A[i][i] = Fraction(1)
            A[i][n] = Fraction(1)

        A[0][0] = Fraction(2)
        x = solve(A, b)

    # result
    for i in range(len(x)):
        if x[i] < 0 or x[i].numerator < x[i].denominator:
            return [-1, -1]

    x[0] *= 2
    return [x[0].numerator, x[0].denominator]

def solve(A, b):
    """
    Solve a linear system Ax = b, adaptive for the matrix in this problem.
    Inputs:
        A - a nxn matrix. n >= 2.
        b - a nx1 vector.
    Returns:
        x - the nx1 vector satisfying Ax = b.
    """
    dim = len(b)

    # A -> Upper triangle
    for i in range(dim - 1):
        if A[dim - 1][i] != 0:
            frac = A[dim -1][i] / A[i][i]
            b[dim - 1] -= frac * b[i]
            A[dim - 1][i] = Fraction(0)
            for j in range(i + 1, dim):
                A[dim - 1][j] -= frac * A[i][j]

    b[dim - 1] /= A[dim - 1][dim - 1]
    A[dim - 1][dim - 1] = Fraction(1)

    # backward subs
    for i in range(dim - 2, -1, -1):
        b[i] -= b[i+1]

    # deal with row 0
    b[0] /= 2

    return b
