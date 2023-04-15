"""  This file implements a solution to the 'Don't Get Volunteered' challenge.

The solution implemented here is straight forward:  Perform a breadth-first
search of all legal moves starting at the begin square.  Keep iterating until
the end location is reached.  The number of iterations in the breadth-first
search is the minimum number of moves to get from the starting to ending
locations.

By using a breadth-first search, all squares that can be reached in n moves are
identified after all squares that can be reached in n-1 moves and before squares
that can be reached in n+1 moves.  This guarantees that the minimum number of
moves is identified.

Since a) the number of squares is constant, b) each square is processed at most
once and c) since the maximum number of moves from a square is at most 8, the
time and space complexity of this solution is O(1).
"""


def bfs(sizes, beg_loc, end_loc):
    """Function bfs() uses a breadth-first search to determine the minimum number
    of moves to get from 'beg_loc' to 'end_loc', where 'beg_loc' and 'end_loc'
    are lists of length 2 with the row and column of the respective positions.
    The size of the board in number of rows and columns is given in length 2 list
    'sizes'."""

    #  Extract input parameters into local variables
    [num_rows, num_cols] = sizes

    [beg_row, beg_col] = beg_loc
    [end_row, end_col] = end_loc

    #  Check for corner case where begin location is also end location
    if (beg_row == end_row) and (beg_col == end_col):
        return 0

    #  Create array to represent number of moves to reach each location on board
    board = []

    for idx0 in range(num_rows):
        board.append([])

        for idx1 in range(num_cols):
            board[idx0].append(' ')

    #  Initialize state variables for bread-first_search
    num_moves = 0
    nxt_locs = [[beg_row, beg_col]]
    board[beg_row][beg_col] = str(num_moves)

    del_r = [-2, -2,  2,  2, -1,  1, -1,  1]
    del_c = [-1,  1, -1,  1, -2, -2,  2,  2]

    #  Perform breadth first search to find the number of moves to reach each location on board
    while 0 < len(nxt_locs):

        #  Update state variables for new iteration
        num_moves = num_moves + 1

        cur_locs = nxt_locs
        nxt_locs = []

        #  For each new location reached in last iteration check locations which can be reached with an additional move
        while len(cur_locs) > 0:
            [cur_row, cur_col] = cur_locs.pop(0)

            #  Loop over all possible moves 
            for idx in range(len(del_r)):

                nxt_row = cur_row + del_r[idx]
                nxt_col = cur_col + del_c[idx]

                if (0 <= nxt_row) and (nxt_row < num_rows) and (0 <= nxt_col) and (nxt_col < num_cols):
                    if ' ' == board[nxt_row][nxt_col]:
                        board[nxt_row][nxt_col] = str(num_moves)
                        nxt_locs.append([nxt_row, nxt_col])

                        #  If this is the end location, return number of moves
                        if (nxt_row == end_row) and (nxt_col == end_col):
                            return num_moves

    return -1


def solution(beg_loc, end_loc):
    """Function solution() computes solutions to the Don't Get Volunteered
    challenge."""

    #  Translate the beginning and ending square numbers into (row,col) pairs
    beg_row = beg_loc // 8
    beg_col = beg_loc % 8

    end_row = end_loc // 8
    end_col = end_loc % 8

    #  Perform breadth first search to find the minimum number of moves
    return bfs([8, 8], [beg_row, beg_col], [end_row, end_col])

