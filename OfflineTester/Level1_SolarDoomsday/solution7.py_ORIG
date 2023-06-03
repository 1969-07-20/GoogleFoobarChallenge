'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://govanify.com/post/foobar/#solar-doomsday"


def get_biggest_square(max_number):
    n=1
    while(n*n < max_number+1):
        n=n+1
    return n-1

def answer(area):
    if(area > 1000000 or area < 1):
        raise ValueError('Area is outside of bounds')
    array=[]
    while(area != 0):
        res=get_biggest_square(area)
        array.append(res*res)
        area-=res*res
        
    return array
