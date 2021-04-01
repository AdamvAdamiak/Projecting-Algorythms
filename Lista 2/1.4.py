import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import *
from scipy.spatial import distance


def showgraph():
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    plt.show()


def us1(A, B):
    structure = {}
    for g in A:
        for u in B:
            if u not in structure.values():
                structure[g] = u
                break
    for g in A:
        if g not in structure.keys():
            A.remove(g)
            us1(A, B)

    return structure


A = ['g1', 'g2', 'g3']
B = ['u1', 'u2', 'u3']

G = nx.Graph()
structure = us1(A, B)
g = list(structure.keys())
u = list(structure.values())
for i in range(0, len(g)):
    for j in range(0, len(g)):
        if j == i+1 or j == i-1:
            continue
        G.add_edge(g[i], u[j])

galleries = list(structure.keys())
utilities = list(structure.values())

for i in range(len(A)-1):
    G.add_edge(galleries[i], galleries[i+1])

showgraph()
