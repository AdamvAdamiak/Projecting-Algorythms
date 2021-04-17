import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import *
from scipy.spatial import distance
from pulp import *


N = 10
K = 10
D = 5
S = 7
R = 4


def dist(G, pos, source, target):
    travel = nx.shortest_path(G, source=source, target=target)
    print(f'Travel from {source} to {target} is {travel}')
    dis = 0
    for i in range(len(travel)-1):
        dis += distance.euclidean(pos[travel[i]], pos[travel[i+1]])
    print(f'Distance between {source} and {target} is {dis}')
    return dis


def solve(N, K, D, S, R):

    leng = N*K
    G = nx.Graph()
    pos = {}
    tmp = 0
    for i in range(leng):
        G.add_node(i)
    for i in range(N):
        for j in range(K):
            pos[tmp] = [i*D, j*D]
            tmp += 1
    for i in range(leng-1):
        if (i+1) % 10 == 0:
            continue
        G.add_edge(i, i+1)

    for i in range(N):
        for j in range(K-1):
            G.add_edge(i+10*j, i+10*(j+1))

    Rs = LpVariable('R', lowBound=0, upBound=R, cat='Integer')
    Ss = LpVariable('S', lowBound=S, cat='Integer')
    prob = LpProblem('problem', LpMaximize)

    nx.draw(G, pos, with_labels=True)
    plt.show()


solve(N, K, D, S, R)
