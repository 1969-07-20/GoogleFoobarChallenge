'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Gargooie/Google_solar_doomsday/blob/master/main.py"


import math

array=[]

def solution(area):
    global array
    array =[]
    area_cut = area 
    
    def take_square(count):
                
        platform = int(math.sqrt(count))
        platform = platform**2
        array.append(platform)
        count = count - platform
        return count

    while area_cut >0 :
        area_cut = take_square(area_cut)

    return(array)


