'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://govanify.com/post/foobar/#ion-flux-relabelling"


def find_item(item,cur,dif):
    right_node=cur-1
    left_node=right_node-dif//2

    if(right_node==item or left_node==item):
        return cur
    else:
        if(item<=left_node):
            return find_item(item,left_node,dif//2)
        else:
            return find_item(item,right_node,dif//2)

def answer(h, q):
    if(h > 30 or h < 1):
        raise ValueError('Height is outside of bounds')
    if(len(q) > 10000 or len(q) < 1):
        raise ValueError('Flux converters list is outside of bounds')

    items=(2**h)-1

    array=[]
    for i in range(len(q)):
        if (q[i]<items and q[i]>0):
            array.append(find_item(q[i],items,items-1))
        else:
            array.append(-1)
    return array
