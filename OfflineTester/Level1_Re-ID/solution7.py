'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/46853104/can-this-solution-to-the-google-foobar-re-id-be-more-efficient (Shaikh Naushad)"


def solution(b):
    bag = "2"
    for num in range(0,20500):
        if num > 1:
            for j in range(2,num):
                if (num % j) == 0:
                    break
                elif len(bag) >= 10006:
                    break
                elif j==num-1:
                    bag += str(num)
                    break
                else:
                    continue

    return bag[b:b+5]
