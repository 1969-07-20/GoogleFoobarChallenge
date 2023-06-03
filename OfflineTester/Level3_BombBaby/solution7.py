'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rudisimo/google-foobar/blob/master/solutions/bomb_baby/solution.py"


#  Mod:
#  - Convert longs to ints


IMPOSSIBLE = "impossible"
THRESHOLD = 100

def multiplier(a, b):
    difference = a - b
    multiplier = (difference / b) + 1
    return multiplier

def answer(M, F):
    step = 0
    mach = int(M)
    facula = int(F)

    try:
        if mach == facula or mach <= 0 or facula <= 0:
            raise ValueError('Incorrect number of bomb types encountered')

        while True:
            if mach <= 0 or facula <= 0:
                raise ValueError('Zero or less bomb types encountered')

            # optimize for large integers
            if mach > THRESHOLD or facula > THRESHOLD:
                if mach > facula:
                    mul = multiplier(mach, facula)
                    mach -= facula * mul
                    step += mul
                elif facula > mach:
                    mul = multiplier(facula, mach)
                    facula -= mach * mul
                    step += mul
                else:
                    raise StopIteration('Same number of bomb types encountered')
            else:
                if mach > facula:
                    mach -= facula
                elif facula > mach:
                    facula -= mach
                else:
                    raise StopIteration('Same number of bomb types encountered')
                step += 1
    except:
        pass

    if mach == 1 and facula == 1 and step >= 0:
        return str(step)
    else:
        return IMPOSSIBLE
