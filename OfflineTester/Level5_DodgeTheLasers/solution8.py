'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/JDMatrix/Google_Foobar/blob/master/Level_5/Dodge_the_Lasers/solution.py"


#  Mod:
#  - Increased precision to 201 digits in order to correctly calculate answer for 200th Pell number + 1


from decimal import Decimal, getcontext
from fractions import Fraction


def solution(n):
    sqr_of_2 = Fraction(Decimal(2).sqrt())
    total = recursion(sqr_of_2, Fraction(n))
    return str(int(total))


def recursion(sqr_of_2, number):
    if number > 0:
        getcontext().prec = 201

        # Important to use int() here instead of Math.floor()
        number_prime = Fraction(int((sqr_of_2 - Fraction(1)) * Fraction(number)))

        return number * number_prime + ((number * (number + Fraction(1))) / Fraction(2)) - (
                (number_prime * (number_prime + Fraction(1))) / Fraction(2)) - recursion(sqr_of_2, number_prime)

    return Fraction(0)
