"""  This file implements a solution to the 'Queue To Do' puzzle.

Description of algorithm:
    The checksum process involves taking the XOR of employee IDs.  This solution
    depends on two key observations.  1)  The ith bit of the final value depends
    on the values of the ith bits of the inputs solely.  The value of the other
    bits of the input have no impact on the ith bit of the result.  2) The XOR
    operation is commutative, so the order in which XORs take place does not
    matter.

    As a result of these two observations, to determine the ith bit of the final
    checksum, it is sufficient to the number of inputs which had a value of 1 in
    the ith bit.  If this number is odd, the ith bit of the checksum is odd; if
    it is even, the ith bit of the checksum is 0.

    This solution processes workers IDs by groups.  For each group it counts the
    number of 1's bits in each bit positions.  Once all groups have been processed
    we know how many 1's appeared in each bit positions.  If for a given bit
    position, that number is odd, the checksum is a 1 othewise it is a 0.

    Since we know that the IDs range from 0 to 2,000,000,000, 31 bits are enough
    to represent all possible IDs.

Time and space complexity of the solution:
    Let L be the value of length passed via the argument list.  The guards process
    L*L workers broken down into L groups of size L.  This solution does O(1) work
    for each group of the L groups of workers.  O(1) space is required by the
    solution.  Therefore, the solution has O(L) time complexity and O(1) space
    complexity.

    It may be possible to directly compute the checksum without considering the
    IDs processed in the queues, potentially reducing the time complexity from
    O(L) to O(1).  But I'm going with this answer under the philosophy that at
    an adequate solution now is often preferable to an excellent solution at
    some unspecified time later.

Assumptions/restrictions:
    This solution assumes that no workers miss work on the day of the automated
    review.

This solution is completely of my own conception and execution.
"""


def counts_to_checksum(bit_count):

    #  Construct the checksum
    checksum = 0
    for count in reversed(bit_count):
        checksum <<= 1;

        if (count % 2) == 1:
            checksum |= 1

    return checksum


def solution(start, length):
    """Compute the checksum of workers at the missing checkpoint to avoid
    detection."""

    #  31 bits is sufficient to represent all possible worker IDs
    num_bits = 31

    #  Precompute values used in bit manipulation operations
    bit_mask0 = [((1 << i)-1) for i in range(num_bits)]
    bit_mask1 = [(1 << i) for i in range(num_bits)]

    #  Define an 'interval' to be a maximal length sequence of contiguous IDs
    #  that all have the same value in the ith bit location.
    int_length = [(1 << i) for i in range(num_bits)]


    #  Initialize counts for each bit position
    bit_count = [0 for i in range(num_bits)]

    #  Process worker's IDs in 'length' batches, each of size 'length'
    for j in range(length):

        #  Determine the number of IDs from this group that get checksummed
        num_checksum = length - j

        #  Get value of first and last ID in the group's checksummed IDs
        id_beg = start + (j * length)
        id_end = id_beg + (num_checksum - 1)

        #  Process IDs in this group
        for i in range (num_bits):
            count = 0

            #  Handle case where the bit can change at most once for this group's
            #  checksummed IDs
            if num_checksum <= int_length[i]:

                #  Get the value of the ith bit of first and last checksummed IDs
                bit_beg = id_beg & bit_mask1[i]
                bit_end = id_end & bit_mask1[i]

                #  Bit i is set for all checksummed IDs
                if (bit_beg != 0) and (bit_end != 0):
                    count = num_checksum

                #  If bit i goes from 1 to 0, count the IDs with 1 at the beginning
                elif (bit_beg != 0) and (bit_end == 0):
                    count = int_length[i] - (id_beg & bit_mask0[i])

                #  If bit i goes from 0 to 1, count the IDs with 1 at the end
                elif (bit_beg == 0) and (bit_end != 0):
                    count = (id_end & bit_mask0[i]) + 1

            # Handle case where the bit can change multiple times for this
            # group's checksummed IDs
            else:
                #  The strategy will be to count the 1's in the whole intervals
                #  and then add in 1's in the possible partial intervals at the
                #  beginning and end of the checksummed IDs.

                #  Express the first ID's location as a pair (interval number,
                #  position within interval)
                int_beg = id_beg // int_length[i]
                res_beg = id_beg & bit_mask0[i]

                #  Get the index of the first whole interval
                if res_beg > 0:
                    whl_beg = int_beg + 1
                else:
                    whl_beg = int_beg

                #  Express the last ID's location ID as a pair (interval number,
                #  position within interval)
                int_end = id_end // int_length[i]
                res_end = id_end & bit_mask0[i]

                #  Get the index of the last whole interval
                if res_end < (int_length[i] - 1):
                    whl_end = int_end - 1
                else:
                    whl_end = int_end
                    res_end = 0

                #  Get the number of 1's in whole intervals
                if whl_end >= whl_beg:
                    num_int = whl_end - whl_beg + 1

                    if ((num_int % 2) == 1) and ((whl_beg % 2) == 1):
                        count = int_length[i] * ((num_int // 2) + 1)
                    else:
                        count = int_length[i] * (num_int // 2)

                #  Add number of bits in the first partial interval
                if (int_beg < whl_beg) and ((int_beg % 2) == 1):
                    count += int_length[i] - res_beg

                #  Add number of bits in the last partial interval
                if (int_end > whl_end) and ((int_end % 2) == 1):
                    count += res_end + 1

            bit_count[i] += count


    #  Return the computed number of checksum
    return counts_to_checksum(bit_count)


#  The following was the first attempt at solving the puzzle.  It is so
#  simple that it was deemed to be almost certain to produce correct
#  answers.  When it failed to pass all tests, failure to produce an
#  answer in the maximum allotted time was thought to be the most
#  likely cause.  So the above solution was created.  The original
#  solution was retained so that it can be used to check the revised
#  solution's answers.  Indeed a bug was found in doing so.

def solution0(start, length):
    """Compute the checksum of workers at the missing checkpoint to avoid
    detection.  Checksum computed via simple but slow simulation method."""

    #  Initialize checksum
    checksum = 0
    id = start

    #  Process workers in batches of length 'length'
    for j in range(length):

        #  Determine cutoff for this batch (decreases by 1 with each batch)
        cutoff = length - j

        #  Process workers in this batch
        for i in range (length):

            #  If a worker's position is before the cutoff, the worker's ID
            #  contributes to the checksum
            if i < cutoff:
                checksum ^= id

            #  Increment ID
            id += 1

        cutoff -= 1

    #  Return the computed checksum
    return checksum


# #  Validate code by computing the answer via two independent methods for a
# #  variety of inputs and compare the answers

# for i in range(1,100):
#     for j in range(0,100):
#         c0 = solution0(i,j)
#         c1 = solution(i,j)

#         if c0 != c1:
#             print "ERROR:  i=%d  j=%d  c0=%d  c1=%d" % (i, j, c0, c1)

# #print(solution(0, 3))
# #  Output:  2

# #print(solution(17, 4))
# #  Output:  14
