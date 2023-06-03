'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/argcag/foobar4/blob/main/foobar4.py"


def solution(numlist):
    counter = 0
    for i in range(len(numlist)): #first number
        for j in range(len(numlist)): #second number
            if numlist[j] % numlist[i] == 0: #check if divisible
                for k in range(len(numlist)): #third number
                    if numlist[k] % numlist[j] == 0: #check if divisible
                        if i < j < k: #check ranges **
                            counter += 1
    return counter

#** program could be made more efficient by reducing the range of the for loop
#to incorporate the i < j < k requirement, omitted for the sake of negligibility.
