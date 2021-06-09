from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def graph_plot(m):
    seed = 1500
    create_using = nx.DiGraph
    G = nx.from_numpy_matrix(np.array(m), create_using=create_using)
    labels = nx.get_edge_attributes(G, 'weight')
    pos = nx.spring_layout(G, seed=seed)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    nx.draw_networkx_edges(G, pos)
    plt.show()

def ford_fulkerson(n, s, t, c):
    '''
    n - liczba wierzcholkow
    s - wierzcholek początkowy
    t - wierzcholek koncowy
    c - macierz pojemnosci
    '''

    INF = float('inf')
    max_flow = 0

    # macierz przeplywow f(u,v) do obliczania pojemnosci rezydualnej
    # cf = c(u,v) - f(u,v) dla krawedzi (u,v)
    f = [[0 for i in range(n)] for i in range(n)]

    # o ile istnieje sciezka od s do t w grafie
    while True:
        graph_plot(c)
        # uzywamy wyszukiwania BFS zeby znalezc sciezke s-t w grafie rezydualnym

        visited = [0 for i in range(n)]
        visited[s] = 1
        q = deque()
        q.append(s)

        while q and visited[t] == 0:
            u = q.popleft()
            for v in range(n):
                cf = c[u][v] - f[u][v]
                if cf > 0 and visited[v] == 0:
                    q.append(v)
                    visited[v] = u


        if visited[t] == 0:  # jeśli nie został osiągniety t
            break

        # rozszerzanie ścieżki s-t w grafie, którą znalezlismy za pomocą BFS
        v = t
        delta = INF
        while True:
            u = visited[v]

            cf = c[u][v] - f[u][v]
            delta = min(delta, cf)
            v = u
            if v == s:
                break

        v = t
        while True:
            u = visited[v]
            print(u)

            f[u][v] += delta
            f[v][u] -= delta
            v = u
            if v == s:
                break
        graph_plot(f)
        #zwiększamy przepływ maksymalny o pojemnosc rezydualną ścieżki
        max_flow += delta
        print("Aktualny maksymalny przepływ = ", max_flow)

    print("Maksymalny przepływ dla zadanego grafu = ", max_flow)

wierzcholki = [0, 1, 2, 3, 4]
n = len(wierzcholki)
pojemnosc = [[0, 5, 3, 0, 0],
            [0, 0, 2, 5, 0],
            [0, 0, 0, 0, 6],
            [0, 0, 3, 0, 5],
            [0, 0, 0, 0, 0]]

ford_fulkerson(n, 0, 4, pojemnosc)



