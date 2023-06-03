'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/zaneaw/Volunteered/blob/main/solution.py"


#  Mod:
#  - Hardwired size of board to 8 at beginning to conform with problem statement.


##############################################################################
####################### Google Foobar Coding Challenge #######################
##############################################################################
# Implementation of Breadth First Search algorithm
from collections import deque
from timeit import default_timer as timer




'''The 2 lists below, when iterated through at the same time, mimic the
    potential movement of a Knight from any Node it's currently at.'''
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]


'''Initiate the Node object to keep track of where the Knight has moved. This
GREATLY cuts down on runtime. The reason is because it stores the moves that
have already been made. This way, we can't retrace our steps and every move
that is made is a new move, progress towards an answer will be made with
every step.'''
class Node:
    count = 0
    def __init__(self, x, y, dist=0):
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.dist = dist  # tracks amount of moves made to get to current point


# Check if the coordinates the Knight is going to are valid
def is_valid(x, y, board):
    return not (x < 0 or y < 0 or x >= board or y >= board)


def solution(start, end):
    board = 8

    # Maximum coordinate on the board
    board_max = board**2 - 1
    start_time = timer()
    try:
        start > board_max or end > board_max or start < 0 or end < 0
    except ValueError as err:
        return "Start point or destination point unreachable. Please try again"
    # Convert the start and end to (x, y) coordinates
    start_x, end_x = start // board, end // board
    start_y, end_y = start % board, end % board
    # Create the objects
    start, end = Node(start_x, start_y), Node(end_x, end_y)
    visited = set()
    # Documentation reference link at bottom
    q = deque()
    # Add 'start' node to the queue
    q.append(start)

    while q:
        node = q.popleft()  # Optimization over q.pop(0)
        x = node.x
        y = node.y
        dist = node.dist
        Node.count += 1
        # Jackpot! We have a match and time to end.
        if x == end.x and y == end.y:
            end_time = timer()
            return dist

        if node not in visited: # Check if node has been added already
            visited.add(node)
            for i in range(8):  # iterate over row and col
                x1 = x + row[i]
                y1 = y + col[i]
                # call is_valid function to ensure coords are on board
                if is_valid(x1, y1, board):
                    q.append(Node(x1, y1, dist + 1))
