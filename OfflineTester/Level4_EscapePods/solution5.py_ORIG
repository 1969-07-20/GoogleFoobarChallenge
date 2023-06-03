'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Li-MingQing/Escape-pods/blob/main/Escape.py"


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    # Using BFS as a searching algorithm
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, sources, sinks):

        max_flow = 0
        for source in sources:
            for sink in sinks:
                parent = [-1] * (self.ROW)
                while self.searching_algo_BFS(source, sink, parent):

                    path_flow = 2000001
                    s = sink
                    #calculating the minimum flow of a path
                    while(s != source):
                        path_flow = min(path_flow, self.graph[parent[s]][s])
                        s = parent[s]

                    # Adding the path flows
                    max_flow += path_flow

                    # Updating the residual values of edges
                    v = sink
                    while(v != source):
                        u = parent[v]
                        self.graph[u][v] -= path_flow
                        self.graph[v][u] += path_flow
                        v = parent[v]

        return max_flow

def solution(entrances, exits, path):
    # Your code here
    g = Graph(path)
    ans = g.ford_fulkerson(entrances, exits)
    return ans
