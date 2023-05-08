'''
The function solution(n) computes the minimum number of operations required to
turn n fuel pellets into 1.  The allowable operations are
- add one pellet
- remove one pellet
- combine pairs of pellets into one pellet which divides the number of
  pellets in half.

These operations work on the least significant bit of the binary representation
of the number of pellets.  One could transform n to 1 by subtracting 1 n-1 times.
But this is slow.  The core of minimizing the number of operations is to divide
by two.  Division by two can only take place when n is even, i.e. when the least
significant bit is 0.

A secondary optimization which minimizes the number of operations concerns how
to turn the least significant (and possibly bits above it) to zero.  Adding one
when the least significant bit is 1 will result in one or more carries.  This
will produce a zero in the least significant bit and a 1 in a higher bit.  But
the carry may convert zero or more 1's to the left of the least significant bit
to zero.

So it is advantageous to harness carry's ability to turn ones to zeros.  This is
done by examining the two least significant bits.
- If the least significant bit is a 0, divide by two.
- If the least and next to least significant bits are 1 and 0, respectively, a
  carry is no use so subtract one.
- If the two least significant bits are 1 then a carry will produce additional
  zeros, reducing the number of operations, except in the case where n=3.
'''


def solution(n):
    #  Convert n from a string to an integer
    n = int(n)

    num_op = 0

    #  Process n, working on the last bit, turning 1's into 0
    #  and eliminating 0 by dividing by two
    while n > 1:
        val = n % 4

        if val == 0:
            n = n // 2
        elif val == 1:
            n -= 1
        elif val == 2:
            n = n // 2
        else:
            if n == 3:
                n -= 1
            else:
                n += 1

        #  Increment the op counter
        num_op += 1

    return num_op


if __name__ == '__main__':
    print (solution(4))
