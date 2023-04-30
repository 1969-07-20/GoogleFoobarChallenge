'''
The function solution(maze) computes solutions to the Prepare the Bunnies'
Escape problem.  Given a maze encoded as a two dimensional list, it
computes the minimum distance between the entrance and exit nodes subject
to the possibility that the distance can be shortened by removing one wall.

The core of the method of finding the solution is to assign a distance of 1
to the nodes at the entrance (exit) and then grow the distances iteratively
until the distances cannot be updated any longer.  Commencing at the starting
node, all nodes reachable from the initial node are assigned a minimum
distance to the starting node.  Visiting nodes in a bread-first order assure
that a) every node is visited once and only once and b) the minimum distance
is assigned to each node.

To find the minimum distance subject to the possibility that one wall is
removed, two sets of distances are computed.  First is the distances of each
node from the maze' entrance.  The second is the distance to the maze' exit.
The minimum distance path passing through any given wall is the minimum of
the sum of the distance to the entrance of a neighboring node on one side
and the distance to the exit of a neighboring node on the opposite side plus
one.  The effect of removing each wall is considered in turn and the minimum
is found.  This is minimum is compared with the minimum distance path of the
path found without removing any walls (which may not exist) to find the
solution.
'''


def solution(maze):

    #  Find the dimensions of the maze
    num_rows = len(maze)
    num_cols = len(maze[0])

    #  Find distances from the space station entrance to the maze
    dist0 = find_dists(maze, 0, 0)

    #  Find distances from the escape pod exit to the maze
    dist1 = find_dists(maze, num_rows-1, num_cols-1)

    #  Determine minimum distance and return it
    return find_path(maze, dist0, dist1)


#  Function find_dists(maze, row_beg, col_beg) records the distances in dist of
#  each open node in maze from the node at (row_beg, col_beg).  This function
#  visits nodes reachable from the starting node in a breadth first traversal.
def find_dists(maze, row_beg, col_beg):

    #  Determine the dimensions of the maze
    num_rows = len(maze)
    num_cols = len(maze[0])

    #  Create empty 2D list to hold distances
    dist = [[None] * num_cols for i in range(num_rows)]

    #  Initialize starting point
    dist[row_beg][col_beg] = 1

    queue = [[row_beg, col_beg]]

    #  Loop until no new distances can be computed
    while len(queue) > 0:

        r, c = queue.pop(0)

        d = dist[r][c]

        #  Consider distance of node to the north
        r0 = r - 1
        c0 = c
        if (r0 >= 0) and (maze[r0][c0] == 0) and (dist[r0][c0] is None):
            dist[r0][c0] = d + 1
            queue.append([r0, c0])

        #  Consider distance of node to the west
        r0 = r
        c0 = c - 1
        if (c0 >= 0) and (maze[r0][c0] == 0) and (dist[r0][c0] is None):
            dist[r0][c0] = d + 1
            queue.append([r0, c0])

        #  Consider distance of node to the south
        r0 = r + 1
        c0 = c
        if (r0 < num_rows) and (maze[r0][c0] == 0) and (dist[r0][c0] is None):
            dist[r0][c0] = d + 1
            queue.append([r0, c0])

        #  Consider distance of node to the east
        r0 = r
        c0 = c + 1
        if (c0 < num_cols) and (maze[r0][c0] == 0) and (dist[r0][c0] is None):
            dist[r0][c0] = d + 1
            queue.append([r0, c0])

    return dist


#  Function find_path(dist0, dist1) finds the minimum distance subject to the
#  possibility of eliminating one wall.
def find_path(maze, dist0, dist1):

    #  Determine the dimensions of the maze
    num_rows = len(maze)
    num_cols = len(maze[0])

    #  If possible initialize minimum distance with distance if no walls are
    #  removed
    if dist0[num_rows-1][num_cols-1] is None:
        min_dist = 2 * num_rows * num_cols
    else:
        min_dist = dist0[num_rows - 1][num_cols - 1]

    #  Loop over nodes.
    for r in range(num_rows):
        for c in range(num_cols):

            #  If this node has a wall evaluate the distances if it's removed
            if maze[r][c] == 1:

                #  Default distances of nodes in the the north, south east and
                #  west to the entrance and exit to large values
                max_dist = 2 * num_rows * num_cols

                d0N = max_dist
                d0E = max_dist
                d0S = max_dist
                d0W = max_dist

                d1N = max_dist
                d1E = max_dist
                d1S = max_dist
                d1W = max_dist

                #  Determine distances of node to the north
                r0 = r - 1
                c0 = c
                if r0 >= 0:
                    if dist0[r0][c0] is not None:
                        d0N = dist0[r0][c0]

                    if dist1[r0][c0] is not None:
                        d1N = dist1[r0][c0]

                #  Determine distances of node to the west
                r0 = r
                c0 = c - 1
                if c0 >= 0:
                    if dist0[r0][c0] is not None:
                        d0W = dist0[r0][c0]

                    if dist1[r0][c0] is not None:
                        d1W = dist1[r0][c0]

                #  Determine distances of node to the south
                r0 = r + 1
                c0 = c
                if r0 < num_rows:
                    if dist0[r0][c0] is not None:
                        d0S = dist0[r0][c0]

                    if dist1[r0][c0] is not None:
                        d1S = dist1[r0][c0]

                #  Determine distances of node to the east
                r0 = r
                c0 = c + 1
                if c0 < num_cols:
                    if dist0[r0][c0] is not None:
                        d0E = dist0[r0][c0]

                    if dist1[r0][c0] is not None:
                        d1E = dist1[r0][c0]

                #  Evaluate distance of north to south path (if any)
                if min_dist > (d0N + d1S + 1):
                    min_dist = (d0N + d1S + 1)

                #  Evaluate distance of south to north path (if any)
                if min_dist > (d0S + d1N + 1):
                    min_dist = (d0S + d1N + 1)

                #  Evaluate distance of west to east path (if any)
                if min_dist > (d0W + d1E + 1):
                    min_dist = (d0W + d1E + 1)

                #  Evaluate distance of east to west path (if any)
                if min_dist > (d0E + d1W) + 1:
                    min_dist = (d0E + d1W + 1)

    return min_dist


if __name__ == '__main__':
#   print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
