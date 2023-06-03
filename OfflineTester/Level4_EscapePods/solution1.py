'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level4_EscapePods/escapePods.py"


'''
The code in this file computes solutions to the Escape Pod challenge.  The
function solution(entrances, exits, path) is called with arguments
- 'entrances' which is an array of room numbers with entrances
- 'exits' which is an array of room number with exits
- 'paths' which is a 2D array with the number of bunnies which can go between
  any pair of rooms.
The function returns the maximum number of bunnies which can go from the
entrance rooms to the exit rooms in one time steps.

It is easy to recognize that this an instance of a max-flow problem.  In fact
the problem statement uses the x/y notation of max-flow problemw where x is
the flow and y is the capacity for an edge.

The Edmonds-Karp is a reasonably simple and efficient algorithm for solving
max-flow problems.  The Wikipedia article at the following link discusses the
Edmonds-Karp algorithm:

https://en.wikipedia.org/wiki/Edmonds-Karp_algorithm

The solution here is based on the pseudo-code for the Edmonds-Karp algorithm
found on the Wikepedia web page.  For completeness the following is the
pseudo-code for the algorithm at that article.

algorithm EdmondsKarp is
    input:
        graph   (graph[v] should be the list of edges coming out of vertex v in the
                 original graph and their corresponding constructed reverse edges
                 which are used for push-back flow.
                 Each edge should have a capacity, flow, source and sink as parameters,
                 as well as a pointer to the reverse edge.)
        s       (Source vertex)
        t       (Sink vertex)
    output:
        flow    (Value of maximum flow)

    flow := 0   (Initialize flow to zero)
    repeat
        (Run a breadth-first search (bfs) to find the shortest s-t path.
         We use 'pred' to store the edge taken to get to each vertex,
         so we can recover the path afterwards)
        q := queue()
        q.push(s)
        pred := array(graph.length)
        while not empty(q)
            cur := q.pop()
            for Edge e in graph[cur] do
                if pred[e.t] = null and e.t != s and e.cap > e.flow then
                    pred[e.t] := e
                    q.push(e.t)

        if not (pred[t] = null) then
            (We found an augmenting path.
             See how much flow we can send)
            df := Infinity
            for (e := pred[t]; e != null; e := pred[e.s]) do
                df := min(df, e.cap - e.flow)
            (And update edges by that amount)
            for (e := pred[t]; e != null; e := pred[e.s]) do
                e.flow  := e.flow + df
            flow := flow + df

    until pred[t] = null  (i.e., until no augmenting path was found)
    return flow
'''

def augment_graph(graph, sources, sinks):
    """augment_graph() augments the graph 'graph' with a super-source and
    a super-sink node which multiplexes the multiple sources and sinks in
    the flow graph into single nodes.

    This function also translates the inputs into data structures that are
    convenient for the Edmonds-Karp implementation which is run on this
    function's outputs."""

    augmented_graph = []

    edges = []

    #  Copy input graph to augmented graph
    for s in range(len(graph)):
        augmented_graph.append([])

        for t in range(len(graph[s])):
            if 0 < graph[s][t]:
                capacity = graph[s][t]

                edge = {
                    'capacity': capacity,
                    'flow':     0,
                    'source':   s,
                    'sink':     t,
                }

                augmented_graph[s].append(edge)

                edges.append(edge)

    #  Augment graph with a 'super source' vertex connected to the sources with
    #  infinite capacity edges to the sources
    augmented_graph.append([])
    a_s = len(augmented_graph) - 1

    for s in sources:
        edge = {
            'capacity': float('inf'),
            'flow':     0,
            'source':   a_s,
            'sink':     s,
        }

        augmented_graph[a_s].append(edge)

        edges.append(edge)

    #  Augment graph with a 'super sink' vertex connected to the sinks with
    #  infinite capacity edges from the sinks
    augmented_graph.append([])
    a_t = len(augmented_graph) - 1

    for t in sinks:
        edge = {
            'capacity': float('inf'),
            'flow':     0,
            'source':   t,
            'sink':     a_t,
        }

        augmented_graph[t].append(edge)

        edges.append(edge)

    #  Return the augmented graph along with the indices for the new source and
    #  sink
    return augmented_graph, a_s, a_t


def edmonds_karp(graph, s, t):
    """edmonds_karp() executes the Edmonds-Karp max-flow algorithm on
    graph 'graph' with source node 's' and sink node 't'.  This function
    returns the maximum flow that can flow through the graph from s to t
    given the capacity limits of the edges."""

    flow = 0

    #  Iterate until no more augmenting paths can be found
    while True:

        #  Use a breadth-first search to find shortest augmenting path
        q = []
        q.append(s)

        pred = [None] * len(graph)

        while 0 < len(q):
            cur = q.pop()

            for e in graph[cur]:
                if (None is pred[e['sink']]) and (e['sink'] != s) and (e['capacity'] > e['flow']):
                    pred[e['sink']] = e
                    q.append(e['sink'])

        #  Break from outer loop if no augmenting path found
        if pred[t] is None:
            break

        #  Found an augmenting path.  See how much flow it can take.
        df = float('inf')

        e = pred[t]

        while True:
            cap_minus_flow = e['capacity'] - e['flow']

            if df > cap_minus_flow:
                df = cap_minus_flow

            e = pred[e['source']]

            if None is e:
                break

        #  And update edges on path by that amount of flow found above.
        e = pred[t]

        while True:
            e['flow'] += df

            e = pred[e['source']]

            if e is None:
                break

        flow = flow + df

    return flow


def solution(entrances, exits, paths):

    #  Augment the flow graph with 'super source' and 'super sink' nodes which
    #  combine multiple sources and sinks into one node
    aug_graph, aug_source, aug_sink = augment_graph(paths, entrances, exits)

    #  Run the Edmonds-Karp algorithm on the augmented graph to compute the
    #  maximum flow
    return edmonds_karp(aug_graph, aug_source, aug_sink)
