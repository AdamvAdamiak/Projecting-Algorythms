from collections import defaultdict
import networkx as nx
from matplotlib import pyplot as plt


class GraphBFS:

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def get_history_queue(self, s):

        visited = [False] * (max(self.graph) + 1)

        queue = []

        queue.append(s)
        visited[s] = True

        history_queue = []

        while queue:

            s = queue.pop(0)

            history_queue.append(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    history_queue.append(i)
                    visited[i] = True
        return history_queue


class GraphDFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def helper_get_visited(self, v, visited, all_checked):

        visited.append(v)

        for neighbour in self.graph[v]:
            all_checked.append(neighbour)
            if neighbour not in visited:
                self.helper_get_visited(neighbour, visited, all_checked)

    def get_visited(self, v):

        visited = []
        all_checked = []

        self.helper_get_visited(v, visited, all_checked)
        return visited


def is_graph_connected(edges, g_DFS):
    for i in edges:
        if i not in list(g_DFS.get_visited(2)):
            return False

    return True


def is_graph_tree(g_DFS, g_BFS, edges):
    if is_graph_connected(edges, g_DFS):
        if len(g_BFS.get_history_queue(2)) == len(edges):
            return True
    return False


def is_graph_forest(edges):
    e = defaultdict(list)
    for t, f in edges:
        e[t].append(f)
        e[f].append(t)

    seen = set()

    def dfs(node, prev):
        if node in seen:
            return False
        seen.add(node)
        for adj in e[node]:
            if adj != prev:
                if not dfs(adj, node):
                    return False
        return True

    for node in e:
        if node not in seen and not dfs(node, -1):
            return False

    return True


def show_graphs():
    G = nx.Graph()
    for i in VV:
        G.add_edge(i[0], i[1])

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)

    plt.show(block=False)
    plt.pause(1)

    for visited in visited_dfs:
        colors = []

        for i in G.nodes():
            if visited == i:
                colors.append('r')
            else:
                colors.append('b')

        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos)

        plt.clf()
        nx.draw(G, pos, node_color=colors, with_labels=True)
        plt.draw()
        plt.pause(1)

    pos = nx.spring_layout(G)
    for visited in visited_bfs:
        colors = []

        for i in G.nodes():
            if visited == i:
                colors.append('r')
            else:
                colors.append('b')

        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos)

        plt.clf()
        nx.draw(G, pos, node_color=colors, with_labels=True)
        plt.draw()
        plt.pause(1)


if __name__ == '__main__':
    V = [0, 1, 2, 3, 4, 5]
    VV = [(0, 1), (1, 0), (0, 2), (1, 2), (2, 1), (2, 0), (2, 3), (
        3, 2), (3, 3), (3, 4), (4, 3), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 1)]

    BFS_G = GraphBFS()
    for i in VV:
        BFS_G.addEdge(i[0], i[1])

    DFS_G = GraphDFS()
    for i in VV:
        DFS_G.addEdge(i[0], i[1])

    visited_bfs = BFS_G.get_history_queue(2)
    visited_dfs = DFS_G.get_visited(2)

    print(f'Odwiedzone wierzchołki w przeszukiwaniu wszerz : ' + str(visited_bfs))
    print(f'Odwiedzone wierzchołki w przeszukiwaniu w głąb : ' + str(visited_dfs))

    print(f'Czy graf jest połączony?: {is_graph_connected(V, DFS_G)}')
    print(f'Czy graf jest drzewem?: {is_graph_tree(DFS_G, BFS_G, V)}')
    print(f'Czy graf jest lasem?: {is_graph_forest(VV)}')

    show_graphs()