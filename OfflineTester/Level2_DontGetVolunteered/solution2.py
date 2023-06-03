'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://hoangyell.com/fb2-google-foobar-gearing-up-for-destruction-dont-get-volunteered"


BOARD_SIZE = 8
AVAILABLE_MOVES = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


class Knight:
    def __init__(self, x=0, y=0, step_count=0, position=None):
        if position:
            x, y = self.position_to_coordinates(position)
        self.x = x
        self.y = y
        self.step_count = step_count

    @property
    def coordinates_to_position(self):
        return self.x + self.y * BOARD_SIZE

    @classmethod
    def position_to_coordinates(cls, position):
        x = position % BOARD_SIZE
        y = int(position / BOARD_SIZE)
        return x, y

    def __hash__(self):
        return self.coordinates_to_position

    def __eq__(self, node):
        return self.x == node.x and self.y == node.y


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.available_moves = AVAILABLE_MOVES

    @classmethod
    def validate_coordidates(cls, x, y):
        return (BOARD_SIZE > x >= 0) and (BOARD_SIZE > y >= 0)

    @classmethod
    def find_way(cls, start, end):
        steps = [start]
        visited = {}
        while steps:
            node = steps.pop(0)
            if node == end:
                return node.step_count
            elif not visited.get(node):
                visited[node] = True
                for offset in AVAILABLE_MOVES:
                    new_x, new_y = node.x + offset[0], node.y + offset[1]
                    if cls.validate_coordidates(new_x, new_y):
                        steps.append(Knight(new_x, new_y, node.step_count + 1))
        return BOARD_SIZE**2 + 1


def solution(src, dest):
    return Board.find_way(Knight(position=src), Knight(position=dest))
