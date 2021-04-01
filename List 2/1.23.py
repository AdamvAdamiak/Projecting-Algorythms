import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import *
from scipy.spatial import distance


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import randint, seed

seed(32)


def plotshow(time):
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show(block=False)
    plt.pause(time)
    plt.close()


def dist(source, target):  # 1.3
    travel = nx.shortest_path(G, source=source, target=target)
    print(f'Travel from {source} to {target} is {travel}')
    dis = 0
    for i in range(len(travel)-1):
        dis += distance.euclidean(pos[travel[i]], pos[travel[i+1]])
    print(f'Distance between {source} and {target} is {dis}')


G = nx.Graph()
nodes = []
XY = []
pos = {}


for i in range(10):
    nodes.append(i)

k = 100
for i in range(10):
    G.add_node(nodes[i])
    Vx = randint(0, k)
    Vy = randint(0, k)
    XY += [[Vx, Vy]]
    pos[nodes[i]] = [Vx, Vy]
    plotshow(.5)

    if(i != 0):
        min = 2*k
        for j in range(i):
            result = round(distance.euclidean(pos[i],pos[j]),2)
            if(result < min):
                node1 = nodes[i]
                node2 = nodes[j]
                min = result
        G.add_weighted_edges_from([(node1, node2, min)])
        plotshow(.5)

print(dist(2, 1))
plotshow(20)

