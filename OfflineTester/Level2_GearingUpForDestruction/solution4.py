'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/hon3g/gearing-up-for-destruction/blob/main/solution.py"


def solution(pegs):
    # Ax = b
    b = distances(pegs) # spaces between pegs
    A_ = adj_mat(b) # adjugate matrix
    x_ = predet_vars(A_, b) # x before 1/det
    det = 1 if len(b) % 2 == 0 else 3 # determinant
    
    ans = [2 * x_[0], det]
    if not_possible(x_, det):
        return [-1, -1]
    elif ans[0] % 3 == 0 and ans[1] == 3:
        return list(map(lambda i: i//3, ans))
    else:
        return ans


def predet_vars(A_, b):
    x_ = []
    for r in A_:
        x_.append(sum([i * j for i, j in zip(b, r)]))
    return x_


def distances(pegs):
    b = []
    for i in range(len(pegs) - 1):
        b.append(pegs[i+1] - pegs[i])
    return b


def adj_mat(b):
    A_ = [[1] * len(b)]
    ones = 1
    for i in range(1, len(b)):
        A_.append([1] * ones)
        A_[i].extend([2] * (len(b) - ones))
        ones += 1
    if len(A_) % 2 == 0:
        A_ = checkerboard(A_, 0)
    else:
        A_ = checkerboard(A_)
        idx = 0
        for r in range(len(A_)):
            A_[r][:idx] = map(lambda i: i * -1, A_[r][:idx])
            idx += 1
    return A_


def checkerboard(A_, d=1):
    sign = 2
    for r in range(len(A_)):
        for c in range(len(A_[0])):
            if sign % 2 != 0:
                A_[r][c] *= -1
            sign += 1
        if d == 0:
            sign += 1
    return A_


def not_possible(x_, det):
    x = list(map(lambda i: i/det, x_))
    return any(n < 0 for n in x)
