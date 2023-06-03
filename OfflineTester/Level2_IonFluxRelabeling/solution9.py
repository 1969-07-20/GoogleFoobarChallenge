'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/adamfarnsworth/IonFluxRelabeling/blob/master/IonFluxRelabeling.py"


#  Mod:
#  - convert return values to integers upon return to caller


import math
def answer(h,q):
    height = h
    fluxConverters = q
    parentList = []*len(q)
    maxValue = 2**height -1
    currentValue = maxValue
    traverseRightOccurred = False

    for i in range(len(q)):
        currentValue = maxValue
        traverseRightOccurred = False
        for j in range(h):
            if(traverseRightOccurred):
                if(fluxConverters[i] == maxValue): # case: root
                    parentList.append(-1)
                    break
                elif(fluxConverters[i] == currentValue - 2**(height - (j+1))): # found value traversing left
                    parentList.append(currentValue)
                    break
                elif(fluxConverters[i] == currentValue-1): # found value traversing right
                    parentList.append(currentValue)
                    break
                elif(fluxConverters[i] < currentValue - 2**(height - (j+1))): # traversing left
                    currentValue = currentValue - 2**(height - (j+1))
                elif(fluxConverters[i] < currentValue-1): # traversing right
                    currentValue = currentValue-1
            else:               # traverse right has not occurred
                if(fluxConverters[i] == maxValue): # case: root
                    parentList.append(-1)
                    break
                elif(fluxConverters[i] == math.floor(currentValue/2)): # found value traversing left
                    parentList.append(currentValue)
                    break
                elif(fluxConverters[i] == currentValue-1): # found value traversing right
                    parentList.append(currentValue)
                    break
                elif(fluxConverters[i] < math.floor(currentValue/2)): # traversing left
                    currentValue = math.floor(currentValue/2)
                elif(fluxConverters[i] < currentValue-1): # traversing right
                    currentValue = currentValue-1
                    traverseRightOccurred = True
    return list(map(int, parentList))
