'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/rishabranjan/foobar_question/blob/master/Solution"


def solution(xs):
    negatives = [num for num in xs if num < 0]
    positives = [num for num in xs if num > 0]
    if len(negatives) == 1 and len(positives) == 0 and xs.count(0) == 0:
        return str(negatives[0])
    if len(negatives) % 2 != 0:
        highestNegative = 0
        for i in range(len(xs)):
            if xs[i] < 0:
                if highestNegative == 0 or xs[i]> highestNegative:
                    highestNegative = xs[i]
        negatives.remove(highestNegative)

    if positives or negatives:
        product = 1
        for x in positives + negatives:
            product = product*x

        return str(product)

    return '0'
