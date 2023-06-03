'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/algomaster99/782b898177ca37bfbf955cec416bb6a4?permalink_comment_id=3827248#gistcomment-3827248 (KaustubhRakhade)"


#  Mod:
#  - Convert answer from numpy array to list upon return to caller.


import numpy as np

# Returns indexes of active & terminal states
def detect_states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    return(active,terminal)

# Convert elements of array in simplest form
def simplest_form(B):
    B = B.round().astype(int).A1                   # np.matrix --> np.array
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum())                      # append the common denom
    return (B / gcd).astype(int)

# Finds solution by calculating Absorbing probabilities
def solution(m):
    active, terminal = detect_states(m)
    if 0 in terminal:                              # special case when s0 is terminal
        return [1] + [0]*len(terminal[1:]) + [1]
    m = np.matrix(m, dtype=float)[active, :]       # list --> np.matrix (active states only)
    comm_denom = np.prod(m.sum(1))                 # product of sum of all active rows (used later)
    P = m / m.sum(1)                               # divide by sum of row to convert to probability matrix
    Q, R = P[:, active], P[:, terminal]            # separate Q & R
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)                            # calc fundamental matrix
    B = N[0] * R * comm_denom / np.linalg.det(N)   # get absorbing probs & get them close to some integer
    return simplest_form(B).tolist()
