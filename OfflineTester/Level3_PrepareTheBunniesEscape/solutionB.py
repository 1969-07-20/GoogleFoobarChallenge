'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://codereview.stackexchange.com/questions/153242/shortest-path-for-google-foobar-prepare-the-bunnies-escape (coderodde)"


#  Mod:
#  - Added a solution() function which in turn instantiated a GridEscapeRouter
#    object which actually calculated the answer.


import time
from collections import deque


class Node:

    def __init__(self, x, y, saldo, grid):
        self.x = x
        self.y = y;
        self.saldo = saldo
        self.grid = grid

    def __hash__(self):
        return self.x ^ self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_neighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        saldo = self.saldo
        grid = self.grid
        rows = len(grid)
        columns = len(grid[0])

        if x > 0:
            wall = grid[y][x - 1] == 1
            if wall:
                if saldo > 0:
                    neighbors.append(Node(x - 1, y, saldo - 1, grid))
            else:
                neighbors.append(Node(x - 1, y, saldo, grid))

        if x < columns - 1:
            wall = grid[y][x + 1] == 1
            if wall:
                if saldo > 0:
                    neighbors.append(Node(x + 1, y, saldo - 1, grid))
            else:
                neighbors.append(Node(x + 1, y, saldo, grid))

        if y > 0:
            wall = grid[y - 1][x] == 1
            if wall:
                if saldo > 0:
                    neighbors.append(Node(x, y - 1, saldo - 1, grid))
            else:
                neighbors.append(Node(x, y - 1, saldo, grid))

        if y < rows - 1:
            wall = grid[y + 1][x]
            if wall:
                if saldo > 0:
                    neighbors.append(Node(x, y + 1, saldo - 1, grid))
            else:
                neighbors.append(Node(x, y + 1, saldo, grid))

        return neighbors


class GridEscapeRouter:

    def __init__(self, grid, saldo):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.saldo = saldo

    def get_escape_route_length(self):
        source = Node(0, 0, self.saldo, self.grid)
        queue = deque([source])
        distance_map = {source: 1}

        while queue:
            current_node = queue.popleft()

            if current_node.x == self.columns - 1 and\
                current_node.y == self.rows - 1:
                return distance_map[current_node]

            for child_node in current_node.get_neighbors():
                if child_node not in distance_map.keys():
                    distance_map[child_node] = distance_map[current_node] + 1
                    queue.append(child_node)

        return 1000 * 1000 * 1000 # Cannot escape


def solution(maze):
   router = GridEscapeRouter(maze, 1)

   return router.get_escape_route_length()
