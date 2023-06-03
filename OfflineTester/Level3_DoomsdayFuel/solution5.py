'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/algomaster99/782b898177ca37bfbf955cec416bb6a4?permalink_comment_id=3972580#gistcomment-3972580 (Dreams-Happen)"


#  Mod:
#  - Fixed problem where Fraction(a,b) wanted rational arguments.


import numpy as np 
import math

from fractions import Fraction

#reference for absorbing Markov Chains: https://math.libretexts.org/Bookshelves/Applied_Mathematics/Applied_Finite_Mathematics_(Sekhon_and_Bloom)/10%3A_Markov_Chains/10.04%3A_Absorbing_Markov_Chains

#code for inverting matrix from https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy

def transposeMatrix(m):
    return map(list,zip(*m))

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

def makeCommonDenominator(lcm, fractions):
    result = []
    for i in range(len(fractions)):
        multiplier = lcm/fractions[i].denominator
        result.append(int(multiplier*fractions[i].numerator))
    result.append(int(lcm))
    return result

def getLCM(fractions):
    denominators = []
    for i in range(len(fractions)):
        denominators.append(fractions[i].denominator)
    lcm = math.lcm(*denominators)
    return lcm
        

def convertToFraction(probabilities):
    result = []
    for i in range(len(probabilities)):
        result.append(Fraction(probabilities[i]))
    return result

def extractProbabilities(fa):
    num_rows, num_cols = fa.shape
    result = []
    for i in range(num_cols):
        result.append(fa[0,i])
    return result
        

def fa(f, a):
    return np.dot(f,a)

def findA(m, numberOfTerminalStates):
    num_rows = len(m) - numberOfTerminalStates
    a = np.zeros((num_rows, numberOfTerminalStates))
    a = a + Fraction()
    for i in range(num_rows):
        for j in range(numberOfTerminalStates):
            a[i,j] = m[i][j+num_rows]
    return a

def calculateFundamentalMatrix(b):
    num_rows, num_cols = b.shape
    i = np.identity(num_rows, int)
    i = i + Fraction()
    difference = np.subtract(i, b)
    #inverse = np.linalg.inv(difference)
    #inverse = difference**(-1)
    inverse = getMatrixInverse(difference)
    return inverse

def findB(m, numberOfTerminalStates):
    dimensionForB = len(m) - numberOfTerminalStates
    b = np.zeros((dimensionForB, dimensionForB))
    b = b + Fraction()
    for i in range(dimensionForB):
        for j in range(dimensionForB):
            b[i, j] = m[i][j]
    return b

def convertMatrixToProbabilities(m):
    result = np.zeros((len(m), len(m)))
    result = result + Fraction()
    for i in range(len(m)):
        denominator = 0
        for j in range(len(m)):
            denominator += m[i][j]
        for j in range(len(m)):
            if(denominator == 0):
                result[i,j] = Fraction(0, 1)
            else:
                result[i,j] = Fraction(Fraction(m[i][j]).limit_denominator(), Fraction(denominator).limit_denominator()) 
    return result

def countTerminalStates(m): 
    numberOfTerminalStates = 0 
    isTerminal = True
    firstTime = True
    for row in m:
        if(isTerminal and (not firstTime)):
            numberOfTerminalStates+=1
        isTerminal = True
        firstTime = False
        for col in row:
            if(col != 0):
                isTerminal = False
    if(isTerminal):
        numberOfTerminalStates+=1
    return numberOfTerminalStates
    
def helper(m):
    numberOfTerminalStates = countTerminalStates(m)
    convertedMatrix = convertMatrixToProbabilities(m)
    b = findB(convertedMatrix, numberOfTerminalStates)
    f = calculateFundamentalMatrix(b)
    a = findA(convertedMatrix, numberOfTerminalStates)
    fA = fa(f,a)
    probabilities = extractProbabilities(fA)
    fractions = convertToFraction(probabilities)
    lcm = getLCM(fractions)
    return makeCommonDenominator(lcm, fractions)            

def solution(m):
    return helper(m)
