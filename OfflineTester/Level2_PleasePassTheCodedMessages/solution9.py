'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.qiniu.com/qfans/qnso-66382333"


def solution(l):
    # Your code here
    if (len(l) == 1 and l[0] % 3 != 0) or (len(l) == 0):
        return 0
    number = formGreatestNumber(l)
    remainder = number % 3
    if remainder == 0:
        result = formGreatestNumber(l)
        return result

    result = removeUnwanted(l, remainder)
    return result


def formGreatestNumber(li):
    li.sort(reverse=True)  # descending order
    li = [str(d) for d in li]  # each digit in string
    number = 0
    if len(li) > 0:
        number = int("".join(li))  # result
    return number


def removeUnwanted(l, remainder):
    possibleRemovals = [i for i in l if i % 3 == remainder]
    if len(possibleRemovals) > 0:
        l.remove(min(possibleRemovals))
        result = formGreatestNumber(l)
        return result
    pairs = checkForTwo(l, remainder)
    if len(pairs) > 0:
        for ind in pairs:
            l.remove(ind)
        result = formGreatestNumber(l)
        return result
    else:
        divisibleDigits = [d for d in l if d % 3 == 0]
        if len(divisibleDigits) > 0:
            result = formGreatestNumber(divisibleDigits)
            return result
        else:
            return 0


def checkForTwo(l, remainder):  # check of (sum of any two pairs - remainder) is divisible by 3
    result = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if ((l[i]+l[j])-remainder) % 3 == 0:
                result.append(l[i])
                result.append(l[j])
                return result
    return []
