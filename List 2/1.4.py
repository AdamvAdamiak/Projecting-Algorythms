import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import *
from scipy.spatial import distance


def showgraph(G):
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

    g = list(structure.keys())
    u = list(structure.values())

    merge_galleries(g)

    merge_galleries_with_utilities(g, u)


def merge_galleries(g):
    for i in range(len(A)-1):
        G.add_edge(g[i], g[i+1])


def merge_galleries_with_utilities(g, u):
    for g1 in range(0, len(g)):
        for g2 in range(0, len(g)):
            if g2 == g1+1 or g2 == g1-1:
                continue
            G.add_edge(g[g1], u[g2])


if __name__ == '__main__':
    A = ['g1', 'g2', 'g3']
    B = ['u1', 'u2', 'u3']

    G = nx.Graph()

    us1(A, B)

    showgraph(G)
