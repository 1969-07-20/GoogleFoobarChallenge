"""  This file implements a solution to the 'The Grandest Staircase Of Them All'
     puzzle.

Description of algorithm:
    Problems of the nature "how many configurations" such as this tend to be
    combinatorial problems.  One pitfall of combinatorial problems is revisiting
    partial solutions repeatedly as one might do when naively enumerating
    all combinations.  Often great advantage can be had by either a) saving
    partial solutions and reusing them or b) aggregating partial solutions.

    The following observation facilitates the aggregation of partial solutions
    for this problem:

    Imagine building the staircase layer by layer from the top layer to the
    bottom, i.e. first place the top layer of bricks, then the second from
    top, then the third from top and so forth until the bottom layer is
    constructed. (Assume Commander Lambda has a gravity nullification device
    which makes construction from top to bottom practical.) The following
    holds true:  the mth layer of bricks either has the same number of
    bricks as the m-1 layer, or it has 1 more brick.

    Now the aggregation:  Create a two dimensional array where the index along
    first dimension corresponds to the number of bricks.  The index along the
    second dimension corresponds to the number of bricks in the base layer.
    The (i,j)th entry in the array gives the number of ways to construct
    staircases with base of size j using i bricks.  Aggregation occurs by
    keeping track of the number of configurations in some equivalence class
    (in this case having i bricks arranged with base j) rather than all of the
    individual individual members of the equivalence class.

    The constraint that each layer of bricks either has the same number of
    bricks as the previous layer or has one more means that the (i,j)th entry
    is the sum of the entries at
        1) (i-j,j) for the case of replicating the previous layer and
        2) (i-j,(j-1)) for the case of increasing the number of bricks in
           the previous layer one.
    (The value i-j as the first index reflects the fact that j bricks are being
    used to construct the base layer.  The values of j and j-1 for the second
    index reflect the fact that the second to last layer can have j or j-1
    bricks.)

    Once the table has been created, the number of ways N bricks can be used to
    create staircases is computed by summing the entries in the table along the
    Nth row.  Lastly, 1 is subtracted to reflect the fact that a stack of N
    bricks arranged as layers all consisting of one brick does not constitute a
    staircase.

Time and space complexity of the solution:
    To determine the answer for N bricks, N rows of the table are constructed.
    The number of entries in the Nth row will be O(sqrt(N)).  (A consequence of
    the fact the sum of integers from 1 to M equals M * (M - 1) / 2 < M*M/2 and
    N = M*M/2 + delta.)

    There are O(N * sqrt(N)) = O(N^(3/2)) non-zero entries in the table, each
    requiring O(1) work to create.  Therefore, creating the table requires
    O(N^(3/2)) work and space.

    The work and space associated with the table dominates the work and space
    required by all other phases of the solution.  Therefore, the solution has
    O(N^(3/2)) time and space complexity.

    The space and time requirements can be optimized, but the problem statement
    limits the problem size to 200 blocks.  The resources this solution requires
    for 200 blocks are very modest.  Therefore, simplicity of logic will be
    favored over optimizing the solution's time and space requirements.

Assumptions/restrictions:
    None

This solution is completely of my own conception and execution.
"""


def solution(n):
    """Compute the number of possible staircase arrangements for a given number
    of bricks n where n is between 3 and 200."""


    #  First upper bound the number of columns in the nth row of the table
    ncol = 0
    sum = 0
    while sum < n:
        ncol += 1
        sum += ncol

    #  Allocate space for the table
    table = [[0 for j in range(ncol+1)] for i in range(n+1)]


    #  Populate the table
    table[1][1] = 1
    for i in range(2,n+1):
        for j in range(1,ncol+1):
            if (i-j) > 0:
                val_a = table[i-j][j]

                if j > 1:
                    val_b = table[i-j][j-1]
                else:
                    val_b = 0

                table[i][j] = val_a + val_b


    #  Sum configurations on the nth row
    sum = 0
    for val in table[n]:
        sum += val

    #  Subtract one for the degenerate configuration of n layers of one block each
    num_config = sum - 1


    #  Return the computed number of configurations
    return num_config



# print(solution(200))
# # Output:  487067745

# print(solution(3))
# # Output:  1
