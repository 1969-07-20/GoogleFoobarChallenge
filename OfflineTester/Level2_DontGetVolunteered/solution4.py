'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/JDMatrix/Google_Foobar/blob/master/Level_2/Dont_Get_Volunteered/solution.py"


BOARD = {}


def init_board_pos(a, b):
    board_pos = {}
    for i in list(range(0, 65, 1)):
        x = i % 8
        y = i // 8
        board_pos[x, y] = i
    return board_pos


def solution(a, b):
    if a == b:
        return 0

    global BOARD
    BOARD = init_board_pos(a, b)

    chart = Graph()
    chart.add_node(a)

    queue = Queue()
    queue.add(chart.nodes.get(a))

    while True:
        current_node = queue.get_next()
        if not current_node.visited:
            current_node.visited = True
            queue.remove()

            for i in valid_moves(current_node.id):
                if i not in chart.nodes.keys():
                    chart.add_node(i)
                    new_node = chart.nodes[i]
                    new_node.dist = current_node.dist + 1
                    current_node.new_edge(new_node, 1)
                    queue.add(new_node)
                if i == b:
                    return new_node.dist


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        self.nodes[key] = Node(key)

    def delete_node(self, key):
        del self.nodes[key]


class Node:
    def __init__(self, id):
        self.id = id
        self.connections = {}
        self.visited = False
        self.dist = 0
        self.x = None
        self.y = None

    def new_edge(self, key, weight):
        self.connections[key] = weight

    def set_coord(self, key):
        self.x = key % 8
        self.y = key // 8

    def get_coord(self):
        return self.x, self.y


class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        self.items.pop(0)

    def get_next(self):
        return self.items[0]


def valid_moves(key):
    up_y = [-2, 2]
    up_x = [-2, 2]

    side_x = [-1, 1]
    side_y = [-1, 1]

    start_x = key % 8
    start_y = key // 8

    moves = []
    for i in up_y:
        for j in side_x:
            new_x = start_x + j
            new_y = start_y + i
            if ((new_x < 8) and (new_x >= 0)) and ((new_y < 8) and new_y >= 0):
                spot = BOARD.get((new_x, new_y))
                moves.append(spot)

    for i in up_x:
        for j in side_y:
            new_x = start_x + i
            new_y = start_y + j

            if ((new_x < 8) and (new_x >= 0)) and ((new_y < 8) and new_y >= 0):
                spot = BOARD.get((new_x, new_y))
                moves.append(spot)

    return moves
