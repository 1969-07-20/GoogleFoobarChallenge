'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/algomaster99/782b898177ca37bfbf955cec416bb6a4?permalink_comment_id=4089220#gistcomment-4089220 (Roma1417)"


def solution(m):
    
    #case when 0 is terminal state
    if(not any(m[0])):
        return [1] + ([0] * (len(m)-1)) + [1]
   
    #diagonal values arent relevant 
    cleanDiagonal(m)
    
    #useful structures
    probabilitiesMatrix = generateProbabilityMatrix(m)
    terminals, notTerminals = getTerminalsAndNotTerminals(m)
    
    #we will remove one by one all of the not-terminals nodes 
    for i in notTerminals:
        absorbNode(probabilitiesMatrix, i)
    
    #now we can take the solution
    terminalsProbabilities = list(map(lambda x: probabilitiesMatrix[0][x], terminals))
    commonDenominator = getCommonDenominator(list(map(lambda x: x[1], terminalsProbabilities)))
    unsimplifiedNumerators = list(map(lambda x: fracUnsimplify(x, commonDenominator)[0], terminalsProbabilities))
    
    return unsimplifiedNumerators + [commonDenominator]
    
   
def cleanDiagonal(m):
    for i in range(len(m)):
        m[i][i] = 0


def generateProbabilityMatrix(m):
    result = []
    for i in range(len(m)):
        result.append([None] * len(m))
        for j in range(len(m)):
            result[i][j] = fracDiv([m[i][j],1], [sum(m[i]),1])
    return result
            
            
def getTerminalsAndNotTerminals(m):
    terminals = []
    notTerminals = list(range(1, len(m)))
    for i in range(len(m)):
        if(not any(m[i])):
            terminals.append(i)
            notTerminals.remove(i)
    return terminals, notTerminals
    
    
def absorbNode(pm, node):
    for i in range(len(pm)):
        for j in range(len(pm)):
            if(i != node and j != node):
                pm[i][j] = fracAdd(pm[i][j], fracMult(pm[i][node], pm[node][j]))
                
    for k in range(len(pm)):
        pm[k][node] = [0, 1]
        pm[node][k] = [0, 1]
        
    for i in range(len(pm)):
        if(pm[i][i] != [0, 1]):
            multiplier = solveGeometricSeries(pm[i][i])
            for j in range(len(pm)):
                if(i == j):
                    pm[i][j] = [0, 1]
                else:
                    pm[i][j] = fracMult(pm[i][j] ,multiplier)
                    
                    
#we will work with fractions, so lets create some functions 

def fracSimplify(a):
    if(a[0] == 0):
        a[1] = 1
    i=2
    while (i <= max(a)):
        if(a[0]%i == 0 and a[1]%i == 0):
            a[0] //= i
            a[1] //= i
        else:
            i += 1
    return a
    
def fracAdd(a, b):
    return fracSimplify([a[0]*b[1] + b[0]*a[1] , a[1]*b[1]])
    
def fracSubs(a, b):
    return fracSimplify([a[0]*b[1] - b[0]*a[1] , a[1]*b[1]])
    
def fracMult(a, b):
    return fracSimplify([a[0]*b[0], a[1]*b[1]])

def fracDiv(a, b):
    if(a[1] == 0 or b[1] == 0):
        return [0, 1]
    return fracSimplify([a[0]*b[1], a[1]*b[0]])

def solveGeometricSeries(r):
    if(r == [1,1]):
        return [1,1]
    n = [1,1]
    d = fracSubs([1,1], r)
    return fracDiv(n, d)
    
def getCommonDenominator(l):
    greater = min(l)
    while(not all(list(map(lambda x: greater % x == 0, l)))):
        greater += 1
    return greater

def fracUnsimplify(a, d):
    return [int(a[0]*(d/a[1])), d]
