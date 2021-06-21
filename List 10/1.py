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
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='gray')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='green')
    nx.draw_networkx_edges(G, pos)
    plt.show()


def ford_fulkerson(liczba_wierzch, wierzcholek_poczatkowy, wierzcholek_koncowy, macierz_pojemnosci):

    INF = float('inf')
    max_flow = 0

    f = [[0 for i in range(liczba_wierzch)] for i in range(liczba_wierzch)]

    while True:
        graph_plot(macierz_pojemnosci)

        visited = [0 for i in range(liczba_wierzch)]
        visited[wierzcholek_poczatkowy] = 1
        q = deque()
        q.append(wierzcholek_poczatkowy)

        while q and visited[wierzcholek_koncowy] == 0:
            u = q.popleft()
            for v in range(liczba_wierzch):
                cf = macierz_pojemnosci[u][v] - f[u][v]
                if cf > 0 and visited[v] == 0:
                    q.append(v)
                    visited[v] = u

        if visited[wierzcholek_koncowy] == 0:
            break

        v = wierzcholek_koncowy
        delta = INF
        while True:
            u = visited[v]

            cf = macierz_pojemnosci[u][v] - f[u][v]
            delta = min(delta, cf)
            v = u
            if v == wierzcholek_poczatkowy:
                break

        v = wierzcholek_koncowy
        while True:
            u = visited[v]

            f[u][v] += delta
            f[v][u] -= delta
            v = u
            if v == wierzcholek_poczatkowy:
                break
        graph_plot(f)
        max_flow += delta
        print("Aktualny przepływ dla grafu wynosi = ", max_flow)

    print("Maksymalny przepływ dla grafu wynosi = ", max_flow)

if __name__ == '__main__':
    wierzcholki = [0, 1, 2, 3, 4]
    n = len(wierzcholki)
    pojemnosc = [[0, 5, 3, 0, 0],
                [0, 0, 2, 5, 0],
                [0, 0, 0, 0, 6],
                [0, 0, 3, 0, 5],
                [0, 0, 0, 0, 0]]

    ford_fulkerson(n, 0, 4, pojemnosc)
