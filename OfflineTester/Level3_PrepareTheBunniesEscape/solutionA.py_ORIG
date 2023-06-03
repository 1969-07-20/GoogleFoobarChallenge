'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/shanejearley/prepare-the-bunnies-escape/blob/master/solution.py"


def shortest_paths(start_x, start_y, map):
    width = len(map[0])
    height = len(map)
    visited = [[None for i in range(width)] for i in range(height)]
    visited[start_x][start_y] = 1

    points = [(start_x, start_y)]
    while points:
        x, y = points.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          next_x, next_y = x + i[0], y + i[1]
          if 0 <= next_x < height and 0 <= next_y < width:
            if visited[next_x][next_y] is None:
                visited[next_x][next_y] = visited[x][y] + 1
                if map[next_x][next_y] == 1 :
                  continue
                points.append((next_x, next_y)) 
                  
    return visited

def solution(map):
    width = len(map[0])
    height = len(map)
    paths_forwards = shortest_paths(0, 0, map)
    paths_backwards = shortest_paths(height-1, width-1, map)

    answer = None
    for i in range(height):
        for j in range(width):
            if paths_forwards[i][j] and paths_backwards[i][j]:
                if answer:
                    answer = min(paths_forwards[i][j] + paths_backwards[i][j] - 1, answer)
                else:
                    answer = paths_forwards[i][j] + paths_backwards[i][j] - 1

    return answer
