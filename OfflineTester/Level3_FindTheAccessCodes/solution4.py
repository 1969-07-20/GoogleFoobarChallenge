'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/fox0088/Find-the-access-codes/blob/master/FindTheAccessCodes.py"


def solution(l):
    ll=len(l)
    arr=[0]*ll
    cnt=0
    for i in range(ll):
        for j in range(i+1,ll):
            if l[j]%l[i]==0:
                arr[j]+=1
                cnt+=arr[i]

    return cnt
