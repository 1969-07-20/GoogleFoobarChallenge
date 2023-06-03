'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/twshutech/fuel-injection-perfection/blob/main/solution.py"


def recursion(n):
  while n > 1:
    global moves
    if n&1 == 0:  #Remain 0 by divide 2.
      n >>= 1
    else:
      if n == 3 or n % 4 ==1:
        n-=1
      else:
        n+=1
    moves+=1

def solution(n):
  look_up = [3, 4]
  foot_print = []
  import math
  global moves, look_up_destination, power_times, is_integer
  is_integer = lambda a: a.is_integer()
  power_times = lambda a:math.log(a, 2)
  look_up_destination = lambda a:a in look_up

  n = int(n)
  moves = 0
  recursion(n)
  return moves
