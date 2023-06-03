'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Burke0/Foobar-Challenge-Find-The-Access-Codes/blob/main/solution.py"


def solution(l):
    # Initialize a list c with zeros to keep track of the count of numbers
    # that l[i] is divisible by
    c = [0] * len(l)
    
    # Initialize a variable count to keep track of the number of lucky triples
    count = 0
    
    for i in range(0, len(l)):
        for j in range(0,i):
            if l[i] % l[j] == 0:
                
                # If l[i] is divisible by l[j], increment the count in the c list
                # for the current index i
                c[i] += 1
                
                # Add the count of numbers that l[j] is divisible by to the count variable
                # to get the total number of lucky triples
                count += c[j] 
    
    return count 
