'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/maximecrevier/foobar3-3/blob/main/foobarlevel3-3.py"


#  Mod:
#  - Fixed problem where Fraction(a,b) wanted rational arguments.


#function to manually solve inverse of matrix
def transposeMatrix(m):
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

#solution code
def solution(m):
    import numpy as np
    from fractions import Fraction

    width_q = len(m)

    for i in m:
        if sum(i) == 0:
            width_q -= 1
    
    #remove terminal states from matrix
    m = [[Fraction(Fraction(v).limit_denominator(),Fraction(sum(i)).limit_denominator()) for v in i] for i in m if sum(i) != 0]

    #solving for block q of matrix m
    q = m[:width_q]
    q = [i[:width_q] for i in q]

    #create identity matrix
    id = np.identity(width_q)
    id = id.astype(int)
    id = id + Fraction()
    
    #solving for block r of matrix m
    r = m[:width_q]
    r = [i[width_q:] for i in r]
    
    #solving for fundamental matrix n
    n = np.subtract(id, q)
    n = getMatrixInverse(n)
    
    #probability matrix b, column n = probabilitities for starting transient state n
    b = np.matmul(n, r)

    [fractions_list] = b[:1].tolist()

    #least common multiple of fractions
    lcm = np.lcm.reduce([fr.denominator for fr in fractions_list])
    
    #formatting output
    vals = [int(fr.numerator * lcm / fr.denominator) for fr in fractions_list]
    vals.append(lcm)


    return vals
