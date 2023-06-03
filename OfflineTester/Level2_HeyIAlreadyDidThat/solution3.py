'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/74421148/google-foo-bar-challenge-hey-i-already-did-that-not-passing-all-the-test-case (Kunjan Rana)"


def convert_to_any_base(num, b): # returns id after converting back to the original base as string
    digits = []
    while(num/b != 0): 
        digits.append(str(num % b))
        num //= b
    result = ''.join(digits[::-1])
    return result

def solution(n, b):
    minion_id_list = [] #list storing all occurrences of the minion id's
    k = len(n)
    while n not in minion_id_list:              # until the minion id repeats
        minion_id_list.append(n)                # adds the id to the list
        x = ''.join(sorted(n, reverse = True))  # gives x in descending order
        y = x[::-1]                             # gives y in ascending order
        if b == 10:                             # if number is already a decimal
            n = str(int(x) - int(y))            # just calculate the difference
        else:
            n = int(x, b) - int(y, b)           # else convert to decimal and, calculate difference
            n = convert_to_any_base(n, b)       # then convert it back to the given base
        n = (k-len(n)) * '0' + n                # adds the zeroes in front to maintain the id length
        if int(n) == 0:                         # for the case that it reaches a constant, return 1
            return 1                           
    return len(minion_id_list[minion_id_list.index(n):]) # return length of the repeated id from
                                                         # first occurrence to the end of the list                                                                        

