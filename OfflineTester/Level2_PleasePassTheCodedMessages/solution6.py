'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/52584048/google-foobar-question-please-pass-the-coded-message (mjames2)"


def solution(l):
    # sort in decending order
    l = sorted(l, reverse = True)
    # if the number is already divisible by three
    if sum(l) % 3 == 0:
        # return the number
        return int("".join(str(n) for n in l))
    possibilities = [0]
    # try every combination of removing a single digit
    for i in range(len(l)):
        # copy list of digits
        _temp = l[:]
        # remove a digit
        del _temp[len(_temp) - i - 1]
        # check if it is divisible by three
        if sum(_temp) % 3 == 0:
            # if so, this is our solution (the digits are removed in order)
            return int("".join(str(n) for n in _temp))
        # try every combination of removing a second digit
        for j in range(1, len(_temp)):
            # copy list of digits again
            _temp2 = _temp[:]
            # remove another digit
            del _temp2[len(_temp2) - j - 1]
            # check if this combination is divisible by three
            if sum(_temp2) % 3 == 0:
                # if so, append it to the list of possibilities
                possibilities.append(int("".join(str(n) for n in _temp2)))
    # return the largest solution
    return max(possibilities)
