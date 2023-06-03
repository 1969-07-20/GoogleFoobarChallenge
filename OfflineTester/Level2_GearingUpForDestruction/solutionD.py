'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/40465866/google-foobar-gearing-up-for-destruction/45626410#45626410 (Playermet)"



def validate(pegs, radius):
  for i in range(1, len(pegs)):
    if radius < 1:
      return False
    radius = pegs[i] - (pegs[i - 1] + radius)
  return True

def solution(pegs):
  if len(pegs) < 2:
    return [-1,-1]
  
  summ = -pegs[0]
  sign = 1
  for i in range(1, len(pegs) - 1):
    summ += pegs[i] * 2 * sign
    sign = -sign
  summ += pegs[-1] * sign
  
  first_r = summ * 2
  divisor = 1

  if len(pegs) % 2 == 0:
    if first_r % 3 == 0:
      first_r /= 3
    else:
      divisor = 3

  if not validate(pegs, first_r / divisor):
    return [-1, -1]
  return [first_r, divisor]
