'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/FoxHub/Google-FooBar/blob/master/Level-2/foobar_2-2_power_hungry.py"


#  Mod:
#  - Per the problem statement, return strings rather than ints


# Foobar Level 2, Challenge 2.

def answer(xs):
    # Notably, in Python 2.5 and beyond, large numbers are already supported
    # without need to cast them to a string.
    positives = [num for num in xs if num>0]
    negatives = [num for num in xs if num<0]
    npos = len(positives)
    nneg = len(negatives)
    energy = 1
    # This captures the case where we have a single negative number, or only a zero.
    # It may not capture the case where we have a negative number and then a string of zeroes.
    if (npos == 0 and nneg == 1) or (npos == 0 and nneg == 0):
        return str(xs[0])
    # Case: No positive numbers.
    elif npos == 0:
        # If we have an odd number of negative numbers, we need to remove the largest.
        if nneg%2 == 1:
            negatives.remove(max(negatives))
            nneg -= 1
        for num in negatives:
            energy *= num
        return str(energy)
    # Case: No negative numbers or one negative number.
    elif nneg == 0 or nneg == 1:
        for num in positives:
            energy *= num
        return str(energy)
    # Case: Multiple positive and negative numbers.
    else:
        if nneg%2 == 1:
            negatives.remove(max(negatives))
        for num in positives:
            energy *= num
        if nneg > 0:
            for num in negatives:
                energy *= num
        return str(energy)
