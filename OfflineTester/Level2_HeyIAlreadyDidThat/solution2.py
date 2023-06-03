'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://blog.ishandeveloper.com/foobar-2020"


#  Mod:
#  - cast output from pow() to int

def dTob(d, b):
    digits = []
    while d > 0:
        digits.insert(0, str(d % b))
        d  = d / b
    return ''.join(digits)

def bTod(b, c):
  n = 0
  for d in str(b):
    n = c * n + int(d)
  return n

def negative(x, y, b):
  if b==10:
    return int(x) - int(y)

  dx=bTod(x,b)
  dy=bTod(y,b)
  dz=dx-dy
  return dTob(dz, b)

def solution(n, b):
    arr=[]
    while True:
        i = "".join(sorted(str(n), reverse=True))
        j = "".join(sorted(str(n)))
        k = negative(i,j,b)

        k2 = len(str(k))
        i2 = len(str(i))

        if (k2) != i2:
            k = k * int(pow(10 ,(i2-k2)))

        for index, item in enumerate(arr):
          if item == k:
            return index + 1
        arr = [k] + arr
        n = k
