'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/barrybardan/queue_to_do_solution/blob/main/solution.py"


from math import log, ceil

def solution(start, length):
    """
    straightforward approach fails 3 tests, prbably because of time limit
    so we need to make XOR trick
    the thing is that we calculate XOR result for each bit position
    to do this we only need number or just parity of sum of all set bits in range
    and then we asseble result from bits
    """
    if length == 1:
        return start
    return predict_result(start, length)

def predict_result(start, length):
    result = 0
    for bit_num in range(0, max_number_of_bits(start, length)+1):
        result += 2**bit_num * predict_one_bit_result(start, length, bit_num)
    return result

def max_number_of_bits(start, length):
    max_num = (start+length**2-1)
    return int(ceil(log(max_num, 2)))+1

def predict_one_bit_result(start, length, bit_num):
    sum_of_bits = 0
    for first_num, last_num in iterate_rows(start, length):
        sum_of_bits += get_sum_of_bits_in_range(first_num, last_num, bit_num)  
    return sum_of_bits % 2

def iterate_rows(start, length):
    for row in range(0,length):
        first_number = start + row * length
        last_needed_number = first_number + length - row
        yield first_number, last_needed_number-1

def get_sum_of_bits_in_range(start, finish, bit_number):
    bits_before_start = predict_sum_of_bits_in_nums_from_zero_to_arg(start-1, bit_number)
    bits_to_finish = predict_sum_of_bits_in_nums_from_zero_to_arg(finish, bit_number)
    return bits_to_finish - bits_before_start

def predict_sum_of_bits_in_nums_from_zero_to_arg(num, bit_number):
    if bit_number == 0:
        return (num+1)//2 
    divisor = 2 ** bit_number
    num -= divisor
    quotient = (num//divisor+1)
    result = quotient * (divisor//2)
    if quotient % 2 == 1:  
        result += num % divisor - 2 ** (bit_number - 1) + 1
    return result
