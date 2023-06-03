'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/shanejearley/hey-i-already-did-that/blob/main/solution.py"


def intToBase(z_int, base_int):
    if z_int == 0:
        return '0'
    digits = []
    while z_int:
        digits.append(int(z_int % base_int))
        z_int //= base_int
    return ''.join(map(str,digits[::-1]))
    
def getNextMinion(minion_id, base_int):
    last_id_asc = ''.join(sorted(minion_id))
    k_int = len(last_id_asc)
    x_int = int(last_id_asc[::-1], base_int)
    y_int = int(last_id_asc, base_int)
    z_int = x_int - y_int
    return intToBase(z_int, base_int).zfill(k_int)
    
def solution(minion_id, base_int):
    index = 0
    minion_dict = {}
    minion_list = []
    minion_dict[minion_id] = index
    minion_list.append(minion_id)
    while True:
        minion_id = getNextMinion(minion_id, base_int)
        if minion_id in minion_dict:
            minion_index = minion_dict[minion_id]
            return len(minion_list[minion_index:])
        index += 1
        minion_dict[minion_id] = index
        minion_list.append(minion_id)
