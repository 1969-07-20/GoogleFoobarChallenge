'''
solution() is a function that determines the length of the cycle when an ID
string ('id') is repeatedly updated in the base ('base') by the algorithm
given in the problem statement.

The function finds the length of the cycle by repeatedly computing new IDs
until it finds the first instance of an ID that repeats.  The length of the
cycle is equal to the number of IDs processed to get to the repeating ID
minus the number of IDs processed before repeating ID was first seen.

This strategy is implemented using a dictionary whose keys are the IDs.  If
an ID is generated but the dictionary already has an entry for the newly
generated ID we know the ID is a repeated ID.

The value stored for each dictionary entry is the number IDs which have been
processed prior to that ID being generated for the first time. Up until the
first repeating ID is encountered, the length of the dictionary is equal to
the number of IDs which have been processed.  When a dictionary entry is
created for a newly encountered ID, the value associated with the key is the
length of the dictionary when the key is added.
'''

def solution(id, base):

    #  Create a dictionary to hold information about IDs which are encountered.
    ids_seen = {id: 0}

    #  Update IDs until an ID is found that repeats
    while True:

        #  Get the next ID
        id = update_id(id, base)

        #  If this ID has been seen break, otherwise record this ID and continue
        if id in ids_seen:
            break
        else:
            ids_seen[id] = len(ids_seen)

    #  Return the length of the cycle
    return (len(ids_seen) - ids_seen[id])

#  Function update_id() uses the algorithm in the problem statement to create
#  the next ID string given the current ID string.
def update_id(id, base):

    #  Calculate x and y
    x = str_baseN_to_int(''.join(sorted(id, reverse=True)), base)
    y = str_baseN_to_int(''.join(sorted(id, reverse=False)), base)

    #  Using x and y create the next ID in the specified base
    next_id = int_to_str_baseN(x - y, base)

    #  Prepend zeros to make the next ID have the same length as the input ID
    next_id = '0' * (len(id) - len(next_id)) + next_id   #  Prepend

    return next_id

#  Function int_to_str_baseN() changes a binary integer ('num') into a string
#  representation in a given base ('base').
def int_to_str_baseN(num, base, digit_symbols="0123456789"):

    digit = digit_symbols[num % base]

    if num == 0:
        return digit
    else:
        return int_to_str_baseN(num // base, base, digit_symbols).lstrip(digit_symbols[0]) + digit


#  Function int_to_str_baseN() changes an integer ('num') represented as a
#  string in given base ('base') into a binary integer.
def str_baseN_to_int(num, base, digit_symbols="0123456789"):

    digit = digit_symbols[:base].index(num[-1])

    if 1 == len(num):
        return digit
    else:
        return str_baseN_to_int(num[:-1], base, digit_symbols[:base]) * base + digit


if __name__ == '__main__':
#   print(solution('1211', 10))
    print(solution('210022', 3))
