'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://livecodestream.dev/challenge/dont-get-volunteered"


import math

def pos_to_coords(pos):
    """
    Converts a position [0..63] into a pair of coord (x, y)
    """
    x = int(math.floor(pos/8))
    y = int(pos%8)
    return (x, y)


def coords_to_pos(x, y):
    """
    Converts a pair of coord (x, y) into a position [0..63]
    """
    return x + y * 8


def get_possible_moves(x, y):
    """
    Returns a list of valid coordinates for next move
    """
    all_moves = []
    all_moves.append((x+2, y+1))
    all_moves.append((x+2, y-1))
    all_moves.append((x-2, y+1))
    all_moves.append((x-2, y-1))
    all_moves.append((x+1, y+2))
    all_moves.append((x+1, y-2))
    all_moves.append((x-1, y+2))
    all_moves.append((x-1, y-2))

    valid_moves = []
    for (x, y) in all_moves:
        if(x >= 0 and x < 8 and y >= 0  and y < 8):
            valid_moves.append((x, y))

    return valid_moves


def solution(src, dest):
    if src == dest:
        return 0

    # Get the current and target tile
    src_x, src_y = pos_to_coords(src)
    dst_x, dst_y = pos_to_coords(dest)
    
    # Create a queue with all the positions I need to check
    queue = get_possible_moves(src_x, src_y)
    depth_queue = []

    # the depth, or solution
    depth = 0 

    while True:
        depth += 1

        # We check each move available at this depth
        for move in queue:
            # Let's see if we arrived to destination
            if move[0] == dst_x and move[1] == dst_y:
                return depth

            # we build the next depth queue, which will replace the queue after we tested them all
            # this is necessary to test one level at a time
            depth_queue.extend(get_possible_moves(move[0], move[1]))

        queue = depth_queue
        depth_queue = []
