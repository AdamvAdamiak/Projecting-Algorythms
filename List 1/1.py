import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def one():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=4)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('A', 'C', weight=3)
    G.add_edge('C', 'D', weight=4)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    plt.show()


def two():
    VV = [1, 2, 3, 4, 5]
    WW = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (3, 5)]
    Vx = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
    Vy = {1: 0, 2: 1, 3: 0, 4: -1, 5: 0}
    g = nx.Graph()
    gpos = {}
    for v in VV:
        g.add_node(v)
        gpos[v] = [Vx[v], Vy[v]]
    for v1 in VV:
        for v2 in VV:
            if (v1, v2) in WW:
                label = str(np.sqrt((Vx[v1] - Vx[v2])** 2 + (Vy[v1] - Vy[v2])**2))
                g.add_weighted_edges_from([(v1, v2, label)])
    nx.draw(g, gpos, with_labels=True, node_color='yellow')
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)
    plt.show()


def three():
    G = nx.Graph()
    n = 24

    for i in range(n-1):
        i = i+1
        for j in range(n-1):
            j = j+1
            if i != j:
                G.add_edge(str(i),str(j))
    
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='yellow')
    #labels = nx.get_edge_attributes(G, 'weight')
    #nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def four():
    G = nx.Graph()
    pos = {}
    pos_tab = []
    counter = 0
    for i in range(250):
        G.add_node(i)
        tmp_pos = (random.randint(0, 25),
                   random.randint(0, 25))
        for j in range(len(pos)):
            pos_tab.append(pos[j])

        if tmp_pos not in pos_tab:
            pos[i] = tmp_pos
            counter = 0
        else:
            counter += 1
            print(counter)
            if counter > 99:
                exit()

            while(tmp_pos in pos_tab):
                tmp_pos = (random.randint(0, 25),
                   random.randint(0, 25))
                if tmp_pos not in pos_tab:
                    pos[i] = tmp_pos
                    counter = 0
                else:
                    counter += 1
                    print(counter)
                    if counter > 99:
                        exit()

    nx.draw(G, pos, with_labels=True, node_color='yellow')
    plt.show()


#one()
#two()
three()
#four()
