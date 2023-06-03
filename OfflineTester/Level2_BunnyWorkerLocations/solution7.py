'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://zhuanlan.zhihu.com/p/469082121"


#  Mod:
#  - Convert answer from float to integer prior to converting it to a string.


def answer(x, y):
  z = ((x+y-1)*(x+y-2))/2 + x
  return str(int(z))
