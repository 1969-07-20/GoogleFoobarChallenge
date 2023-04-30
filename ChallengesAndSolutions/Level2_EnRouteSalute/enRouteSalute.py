"""  This file computes solutions to the "En Route Salute" challenge.

The solution implemented here is based on the following observations:
1) Since minions which travel the same direction don't pass each other they
   don't salute each other.
2) Because of the above, the same number of salutes would be generated if all
   minions going one direction were replaced with stationary minions and only
   minions going in the other direction moved.  The same result is produced
   whether left-going or right-going minions are replaced with stationary
   minions.  This implementation treats right-going minions as stationary.
3) The number of right-going minions a left-going minion passes is equal to the
   number of minions to the left of its position in the string.
4) Each passing of minions generates two salutes.

Given the above observations, the strategy used by the solution here is simple:
Scan the string from left to right.  When a '>' character is encountered,
increment a counter of the number of right-going minions.  When a '<' character
is encountered increment a counter of the number of solutes by twice the counter
of right-going minions.  When the right end of the string is reached, the salute
counter has the solution to the challenge.
"""


def solution(s):
    """Function solution(s) computes solutions to the "En Route Solute"
    challenge.  Given input s which is a string which represents a hallway with
    minions travelling either left '<' or right '>', solutions returns the
    total number of solutes made by the minions traveling the hallway.
    """

    num_right = 0
    num_salute = 0

    #  Scan string from left to right counting the number of salutes
    for c in s:
        if '>' == c:
            num_right = num_right + 1
        elif '<' == c:
            num_salute = num_salute + 2 * num_right

    return num_salute

