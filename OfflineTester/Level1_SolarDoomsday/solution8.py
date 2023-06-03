'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "http://sidtone.com/solar-doomsday"


'''
Created on Feb 15, 2017
 
 
 
@author: Tony Harrell
'''
import math;
 
 
 
def answer(area):
    fList = [];
 
 
 
    solarPanelCalc(area, fList);
    fList.reverse();
    return fList;
 
 
 
def solarPanelCalc(area, fList):
    pArea = 0;
 
 
 
    if area >= 1 and area <= 1000000:
        tmp = int(math.sqrt(area));
        if tmp <= 0:
            return pArea;
        else:
            pArea = int(math.pow(tmp, 2));
            nArea = area - pArea;
            solarPanelCalc(nArea, fList);
            fList.append(pArea);
        return pArea;
