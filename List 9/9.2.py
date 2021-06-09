import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


graph = {0: {3: 5, 4: 3},
         1: {2: 1, 5: 1, 4: 5},
         2: {1: 1, 5: 2},
         3: {5: 3, 6: 3, 0: 5},
         4: {1: 5, 6: 1, 0: 3},
         5: {2: 2, 3: 3, 1: 1, 4: 5},
         6: {4: 1, 3: 3},
         7: {}}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    visited = {}
    unvisited = graph
    infinity = 9999999
    path = []
    for node in unvisited:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    # wykonujemy dopoki nie zostaną sprawdzone wszystkie wierzcholki
    while unvisited:
        minNode = None
        for node in unvisited:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + \
                    shortest_distance[minNode]
                visited[childNode] = minNode
        unvisited.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = visited[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


dijkstra(graph, 2, 0)


edges = [(1, 2, 1), (2, 5, 2), (3, 5, 3),
         (5, 1, 1), (4, 1, 5), (4, 6, 1),
         (4, 0, 3), (3, 7, 5), (0, 5, 3)]


G = nx.Graph()

G.add_weighted_edges_from(edges)
labels = nx.get_edge_attributes(G, 'weight')
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()
