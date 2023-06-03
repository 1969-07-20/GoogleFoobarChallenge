'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/eric-meehan/Queue-To-Do---Python/blob/main/Queue%20To%20Do%20-%20Python/main.py"


"""
Eric Meehan
2020-11-20

Queue To Do
"""

import sys

def SequentialXOR(n):
    # Executing an XOR over sequential numbers starting with 1 returns a pattern of n, 1, n+1, 0
    # This function simulates this pattern
    switch = [n, 1, n + 1, 0]
    return switch[n % 4]

def Table(Start, Length):
    # Defines the end points for each row of the table
    return [Start + (Length * (i + 1) - (i + 1)) for i in range(Length)]
    
def XORRows(Start, End):
    # Finds the XOR for a row by performing the operation XOR(XOR(1 - StartOfRow), XOR(1 - EndOfRow))
    """
    Given that an XOR between any number and itself is 0, and an XOR between any number and 0 is itself, This function finds the cumulative XOR quickly by using the pattern defined in SequentialXOR to XOR the Start and End of each row - the results of which are a negation of the overlapping numbers (1 - Start).
     """
    if Start > 0:
        Start -= 1
    return SequentialXOR(Start) ^ SequentialXOR(End)
    

def solution(Start, Length):

    # Generate the table
    table = Table(Start, Length)

    # Create the cumulative XOR checksum
    CumulativeXOR = 0

    # Use the SequentialXOR function on each row, combining the result with the CumulativeXOR
    for i in range(Length):
        CumulativeXOR ^= XORRows((Start + (Length * i)), table[i])

    # Return the result
    return CumulativeXOR
