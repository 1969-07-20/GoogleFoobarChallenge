'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://blog.finxter.com/googles-foobar"


def solution(l):
    x = find_largest_bucket(l)
    return find_max_number(x)
    

def find_largest_bucket(l):
    
    ''' Are the digits in the list divisible?'''
    if sum(int(digit) for digit in l)%3 == 0:
        return l
    
    ''' Find all smaller buckets recursively '''
    buckets = []  
    for digit in l:
        if digit not in {0, 3, 6, 9}:
            tmp = l[:]
            tmp.remove(digit)
            buckets.append(find_largest_bucket(tmp))
    
    largest_bucket = max(buckets, key=find_max_number)
    return largest_bucket


def find_max_number(l):
    '''Returns maximal number that can be generated from list.'''
    sorted_list = sorted(l)[::-1]
    number = ''.join(str(x) for x in sorted_list)
    return int(number)
