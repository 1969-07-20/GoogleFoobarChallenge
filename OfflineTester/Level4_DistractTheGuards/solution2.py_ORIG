'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://pages.cs.wisc.edu/~shrey/2020/08/10/google-foobar.html"


def solution(l):
    g = generate_graph(l)
    matches = reduce(g)
    return len(l) - matches

def loop(x,y):
    base = int((x+y)/gcd(x,y))
    return bool(base & (base - 1))

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def generate_graph(l):
    G = {i: [] for i in range(len(l))}
    for i in range(len(l)):
        for j in range(i, len(l)):
            if i != j and loop(l[i], l[j]):
                G[i].append(j)
                G[j].append(i)
    return G

def reduce(g):
    matched = 0
    checks = len(g[max(g, key=lambda key: len(g[key]))])
    while len(g) > 1 and checks >= 1:
        init_mw_node = min(g, key=lambda key: len(g[key]))
        if (len(g[init_mw_node])) < 1 :
            del g[init_mw_node]
        else:
            temp_sec_min = [len(g[g[init_mw_node][0]])+1,1]
            for node_i in g[init_mw_node]:
                if len(g[node_i]) < temp_sec_min[0]:
                    temp_sec_min = [len(g[node_i]), node_i]
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == init_mw_node:
                        del g[node_i][check_i]
                        break
            for node_i in g[temp_sec_min[1]]:
                for check_i in range(len(g[node_i])):
                    if g[node_i][check_i] == temp_sec_min[1]:
                        del g[node_i][check_i]
                        break
            del g[init_mw_node]
            del g[temp_sec_min[1]]
            matched += 2
        if len(g) > 1:
            checks = len(g[max(g, key=lambda key: len(g[key]))])
    return matched
