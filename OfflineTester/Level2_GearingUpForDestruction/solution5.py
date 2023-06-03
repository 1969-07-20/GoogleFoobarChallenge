# -*- coding: utf-8 -*-

'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/wrbyepct/Gearing-up-for-destruction/blob/main/solution_revised.py"


from fractions import Fraction

"""
Important question! 
    Does every gear has a valid radius?
"""

"""
Informal Structured Outline


Problem type:
    Matching restrictions


The gist of the problem: 
    Given the distance of each pegs
    1. I have to fit the gears tightly on each pegs
    2. Also the first gear's radius has to be twice as the last gear's


Input range:
    A list of positive integers
    2 ≤ list size ≤ 20


Mainly concerned target:
    1. Legal relation of every neighbor two gears
    2. Special relation of the first and the last gear

Goal:
    1. Every gear has positive radius greater than or equal to 1, COULD be real number
    2. Spot the hidden relation of the first and the last gears


What we have known:
   Let's say [2, 10, 11, 13] is the list of pegs, and the potential gear radii are G1, G2, G3, Gn
             [4, 30, 50] is another list pegs. and the potential gear radii are G1, G2, Gn

   1. So the distance between of the second(b) and the first(a) peg is just b - a
        E.g.
            Every distance of 2 neighbor pegs is 8(10 -2), 1(11 - 10), 2(13 - 11) in the first example
            26(30 -4), 20(50 - 30) in the second example

   2. Then if every 2 gears has to be tightly fit, the sum of their radii has to be their peg distance
       E.g.
            For the first example:          For the second example:
                G1 + G2 = 8                     G1 + G2 = 26
                G2 + G3 = 1                     G2 + Gn = 20
                G3 + Gn = 2     

   3. In order to cancel the gears other than G1 and Gn,
      we can do some simple addition and subtraction, 
      then we can find that:
         For the first example:
            G1 + Gn = 9(8 - 1 + 2)
         For the second example:
            G1 - Gn = 6(26 - 20)

   4. We know that G1 + Gn is actually 3 * Gn (because G1 is twice bigger than Gn)
               and G1 - Gn is Gn 





Conclusion: 
    1. If we have even number of pegs -> G1 + Gn = FPDD    
       If we have odd number of pegs -> G1 - Gn = FPDD
    2. The final product of distance difference is always:
            a - b + c - d ... n(alternating - & +)
    3. With the fact that the radius of G1 has to be twice as Gn,
            We are able to determine the potential G1 radius        

Must do in order to achieve the goal: 
    I have to know:
        1. Every 2 neighbor pegs distance
        2. The final product of distance difference(FPDD)
        3. Is it odd or even number of pegs?:
                Even -> G1(2 * Gn) + Gn = 3Gn = FPDD
                Odd -> G1(2 * Gn) - Gn = Gn = FPDD
        4. Does my result fit the limitation? (Every gear has radius of at least 1)        

===============================================================

Formal Description


-------------Definitions--------------
pegs: List:Int
distances: List:Int
FPDD: Int

G1: Fraction
first_gear_fraction: List:Int


---------------Steps-------------------
distances := get_distances(pegs);
FPDD := get_FPDD(distances)
first_gear_fraction := [-1, -1]
{ True }
IF 
    FPDD < 1 -> skip
    FPDD ≥ 1 ->                                                                 
        // G1 + Gn = 3Gn
        pegs_is_even(pegs) -> 
            IF            
                G1 := 2 * Fraction(FPDD / 3); 
                IF
                    // Make sure every gear is ≥ 1
                    is_valid(G1, distances) -> 
                        first_gear_fraction := [G1.numerator, G1.dominator]
                   ¬is_valid(G1, distances) ->
                        first_gear_fraction := [-1, -1]
                FI   
            FI
        // G1 - Gn = Gn 
       ¬pegs_is_even(pegs) -> 
            IF           
                G1 := 2 * Fraction(FPDD);
                IF
                    // Make sure every gear is ≥ 1
                    is_valid(G1, distances) -> 
                        first_gear_fraction := [G1.numerator, G1.dominator]
                   ¬is_valid(G1, distances) ->
                        first_gear_fraction := [-1, -1]
                FI 
            FI    
FI   

{ first_gear_fraction = [-1, -1] ∨ (first_gear_fraction[0] ≥ 1 ∧ first_gear_fraction[1] ≥ 1) }


"""

def solution(the_list):
    distance_list = get_distance_for_every_two_pegs(the_list)
    alternating_sum = get_alternating_sum(distance_list)  # FPDD

    first_gear_in_fraction = Fraction(alternating_sum * 2, 3) if list_is_even(the_list) \
        else Fraction(alternating_sum * 2)

    return [-1, -1] if found_invalid_radius(first_gear_in_fraction, distance_list) \
        else [first_gear_in_fraction.numerator, first_gear_in_fraction.denominator]


def list_is_even(the_list):
    """
    Returns True if given list is even size; otherwise returns False
    """
    return len(the_list) % 2 == 0


def get_distance_for_every_two_pegs(the_list):
    """
    Given a list of integers, returns a list of list[i + 1] - list[i]
    """
    list_range = [i for i in range(len(the_list) - 1)]
    return list(map(lambda i: the_list[i + 1] - the_list[i], list_range))


def get_alternating_sum(distance_list):
    """
    Given a list of real numbers, returns list[i] + (- list[i+1]) + list[i+2] + .....
    """
    distance_alternating_sum = 0
    toggle = 1
    for distance in distance_list:
        distance_alternating_sum += (distance * toggle)
        toggle *= -1
    return distance_alternating_sum


def found_invalid_radius(first_gear, distance_list):
    """
    Given the radius of the first gear, and the distance list, deduce the radius of every gear
    If there's a radius less than 1, returns True; otherwise returns False
    """
    checking_gear = first_gear
    for distance in distance_list:
        if checking_gear < 1:
            return True
        checking_gear = distance - checking_gear
    return False
