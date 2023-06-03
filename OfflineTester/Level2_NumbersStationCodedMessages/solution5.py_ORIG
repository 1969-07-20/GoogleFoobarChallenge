'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/raghavpatnecha/Foobar/blob/master/Number%20Station%20Coded%20Message/number_station_coded_message.py"


def answer(l, t):

    input_list = l
    target = t

    summed_num = 0
    result = []

    for i, elm in enumerate(input_list):

        for j in range(i, len(input_list)):

            summed_num += input_list[j]

            if summed_num == target:

                result.append([i, j])

        summed_num = 0

    if len(result) == 0:
        return [-1, -1]
    else:
        return result[0]
