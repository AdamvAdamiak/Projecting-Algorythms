import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
inf = float('inf')

M = [[inf, inf, inf, 5, 3, inf, inf, 4],
     [inf, inf, 1, inf, 5, 1, inf, inf],
     [inf, 1, inf, inf, inf, 2, inf, inf],
     [5, inf, inf, inf, inf, 3, 3, inf],
     [3, 5, inf, inf, inf, inf, 1, inf],
     [inf, 1, 2, 3, inf, inf, inf, inf],
     [inf, inf, inf, 3, 1, inf, inf, inf],
     [4, inf, inf, inf, inf, inf, inf, inf]]

M_copy = [[-1, -1, -1, 5, 3, -1, -1, 4],
     [-1, -1, 1, -1, 5, 1, -1, -1],
     [-1, 1, -1, -1, -1, 2, -1, -1],
     [5, -1, -1, -1, -1, 3, 3, -1],
     [3, 5, -1, -1, -1, -1, 1, -1],
     [-1, 1, 2, 3, -1, -1, -1, -1],
     [-1, -1, -1, 3, 1, -1, -1, -1],
     [4, -1, -1, -1, -1, -1, -1, -1]]

G = nx.Graph()

def floyd_warshall(graf, a, b):
    for x in range(len(graf)):
        for i in range(len(graf)):
            for j in range(len(graf)):
                graf[i][j] = min(graf[i][j], graf[i][x]+graf[j][x])
    print(graf[a][b])




G = nx.from_numpy_array(np.array(M_copy))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
floyd_warshall(M, 2, 7)
plt.show()



