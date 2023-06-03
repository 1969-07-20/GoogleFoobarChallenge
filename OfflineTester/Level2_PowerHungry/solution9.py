'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rudisimo/google-foobar/blob/master/solutions/power_hungry/solution.py"


def answer(xs):
    # handle simple edge cases
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])

    # split input into positive/negative lists
    positive_numbers = []
    negative_numbers = []
    for n in xs:
        if n > 0: positive_numbers.append(n)
        elif n < 0: negative_numbers.append(n)

    # cache list counts
    positive_count = len(positive_numbers)
    negative_count = len(negative_numbers)

    # handle single negative panel edge case
    if negative_count == 1 and positive_count == 0:
        return str(0)

    # handle all zeros edge case
    if negative_count == 0 and positive_count == 0:
        return str(0)

    # calculate positive power output
    power_output = 1
    for n in positive_numbers:
        power_output *= n

    # remove "largest" negative panel in odd arrangements
    if negative_count % 2 == 1:
        negative_numbers.remove(max(negative_numbers))

    # calculate negative power output
    for n in negative_numbers:
        power_output *= n

    return str(power_output)
