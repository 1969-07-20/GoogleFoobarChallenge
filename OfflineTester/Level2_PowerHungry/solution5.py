'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/sdkrystian/Google-Foobar/blob/master/PowerHungry.py"


#  Mod:
#  - Corrected one instance where answer was returned as an int not string


def answer(xs):
    nums = []
    negs = []
    maxpower = 1
    if (max(xs) == 0 and min(xs) < 0):
        return str(0)
    if (max(xs) == 0 and min(xs) == 0):
        return str(0)
    for i in xs:
        if (i != 0):
            nums.append(i)  
            if i < 0:
                negs.append(i)
    if (max(nums) < 0 and len(nums) == 1):
        return str(nums[0])
    if (len(negs) % 2 == 1 and len(negs) >= 1):
        negs.sort()
        nums.remove(negs[len(negs) - 1])
    for i in nums:
        maxpower *= i
    return str(maxpower)
