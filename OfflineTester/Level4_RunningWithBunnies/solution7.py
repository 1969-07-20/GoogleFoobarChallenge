'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/JDMatrix/Google_Foobar/blob/master/Level_4/Running_with_Bunnies/solution.py"


def solution(n, time_limit):
    graph = {}

    for i, level in enumerate(n):
        new_node = Node(i)
        for j, col in enumerate(level):
            if i != j:
                new_node.add_connection(j, col)
        if i == 0:
            new_node.set_start()
        elif i == len(n) - 1:
            new_node.set_hatch()
        else:
            new_node.set_bunny()

        graph[i] = new_node

    for i in graph.keys():
        node = graph.get(i)
        for connection_id in node.connections.keys():
            node.add_connection_nodes(connection_id, graph[connection_id])

    for i in graph.keys():
        node = graph.get(i)
        best_dist, cycle = bellman_ford(node, graph, n)
        if cycle:
            list_final = []
            for j in range(1, len(n) - 1):
                list_final.append((j - 1))
            return list_final
        else:
            node.bf_dist = best_dist

    global best
    best = []

    max_bunnies(graph[0], time_limit, [], n)

    best = [i - 1 for i in best]
    best = sorted(best)

    return best


def bellman_ford(start, graph, n):
    """Implementation of Bellman-Ford algorithm to find shortest path from node to all other nodes in
    a weighted graph where weights can be negative and it supports cycles."""

    final_cost = {}
    cycle = False
    edges = []

    for j in graph.keys():
        final_cost[j] = float('inf')

    for row_counter, row in enumerate(n):
        for col_counter, col in enumerate(row):
            edges.append([row_counter, col_counter, col])

    for i in range(0, len(graph.keys()) - 1):

        final_cost[start.id] = 0
        for next_edge in edges:

            current_node = next_edge[0]
            next_node = next_edge[1]
            cost_edge = next_edge[-1]

            if final_cost[current_node] + cost_edge < final_cost[next_node]:
                final_cost[next_node] = final_cost[current_node] + cost_edge

    for i in range(0, len(graph.keys()) - 1):

        for next_edge in edges:

            current_node = next_edge[0]
            next_node = next_edge[1]
            cost_edge = next_edge[-1]
            if final_cost[current_node] + cost_edge < final_cost[next_node]:
                final_cost[next_node] = final_cost[current_node] + cost_edge
                cycle = True

    del final_cost[start.id]
    return final_cost, cycle


def max_bunnies(current, budget, basket, n):
    exit_id = len(n) - 1

    global best
    if len(basket) > len(best):
        best = basket

    for connections_id in current.bf_dist.keys():
        next_node = current.connection_nodes.get(connections_id)
        if next_node.bunny and next_node.id not in basket:
            if budget - current.bf_dist.get(next_node.id) - next_node.bf_dist.get(
                    exit_id) >= 0:
                max_bunnies(next_node, budget - current.bf_dist.get(next_node.id), basket + [next_node.id], n)
    return


class Node:

    def __init__(self, id):
        self.id = id
        self.cost_origin = float('inf')
        self.connections = {}
        self.connection_nodes = {}
        self.bunny = False
        self.hatch = False
        self.start = False
        self.bf_dist = None

    def set_bunny(self):
        self.bunny = True

    def set_hatch(self):
        self.hatch = True

    def set_start(self):
        self.start = True

    def add_connection(self, connection_id, cost):
        self.connections[connection_id] = cost

    def add_connection_nodes(self, connection_id, node):
        self.connection_nodes[connection_id] = node

    def connection_list(self):
        return self.connection


class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_next(self):
        return self.items.pop(0)

    def get_size(self):
        return len(self.items)
