import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import *
from scipy.spatial import distance
# ciągi liczbowe


def x1(n):
    if n == 0:
        return 0
    return(pow(3, n) + x1(n-1))


def x2(n):
    if n == -1 or n == 0:
        return 0
    return(n + x2(n-2))


def x3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return(x3(n-1) + x3(n-2))

# print(x1(5))
# print(x2(5))
# print(x3(5))

# Grafy


def one(n, V):
    G = nx.Graph()
    pos = {}
    seed(10)
    for v in V:
        G.add_node(v)
        pos[v] = [randint(0, 100)*random(), randint(0, 100)*random()]

    for v in V:
        euclidian_distances = {}
        for vv in V:
            if vv == v:
                continue
            euclidian_distances[vv] = distance.euclidean(pos[v], pos[vv])
        minimum_distance = min(euclidian_distances,
                               key=euclidian_distances.get)
        G.add_edge(v, minimum_distance, weight=round(
            euclidian_distances[minimum_distance], 2))

    nx.draw(G, pos, with_labels=True, node_color='yellow')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    def dist(source, target): #two
        travel = nx.shortest_path(G, source=source, target=target)
        print(travel)
        dis = 0
        for i in range(len(travel)-1):
            dis += distance.euclidean(pos[travel[i]], pos[travel[i+1]])
        print(dis)
    dist(13, 32)


n = 100
V = []
for i in range(n):
    V.append(i+1)
one(n, V)
