

from collections import defaultdict


import networkx as nx
from matplotlib import pyplot as plt
from networkx import Graph


class GraphTopological:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.stack = []
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def helper_topologicalSort(self, v, visited, stack):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.helper_topologicalSort(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):

        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.helper_topologicalSort(i, visited, stack)
        self.stack = stack
        return stack

    def get_stack(self):
        return self.stack


def calculate_job_time(time, best_sequence, edges_connections):

    jobs = [[i, list(edges_connections[i].keys()), None]
            for i in best_sequence]
    time = [time[i] for i in best_sequence]
    current_time = 0
    result = []

    for i in range(len(jobs)):

        job_processing = jobs[i]

        if job_processing not in result:

            if len(jobs) == i + 1:
                job_processing[2] = current_time
                result.append(job_processing)
            e = 0
            while job_processing is not None and len(jobs) > i + e + 1:
                e += 1
                next_job = jobs[i + e]

                if next_job[0] not in job_processing[1] and job_processing[0] not in next_job[1]:
                    job_processing[2] = current_time
                    result.append(job_processing)
                else:
                    job_processing[2] = current_time
                    result.append(job_processing)
                    job_processing = None
            current_time += time[i]
    return result


def define_topological_graph():
    g = GraphTopological(len(time))
    for i in edges:
        g.addEdge(i[0], i[1])
    g.topologicalSort()
    return g


def define_graph():
    G = Graph()
    for i in edges:
        G.add_edge(i[0], i[1])
        G.add_edge(i[1], i[0])
    pos = nx.spring_layout(G)
    return G, pos


if __name__ == '__main__':
    time = [10, 15, 7, 9, 10, 11, 12]
    edges = [(3, 6), (5, 2), (4, 0), (4, 1), (2, 3), (3, 4)]

    g = define_topological_graph()
    fig1, ax1 = plt.subplots(1, 1)
    fig2, ax2 = plt.subplots(1, 1)
    print('Operacje posortowane topologicznie: ', g.get_stack())
    G, pos = define_graph()

    nx.draw_networkx_nodes(G, pos, node_size=500, ax=ax1)
    nx.draw_networkx_labels(G, pos, ax=ax1)
    nx.draw_networkx_edges(G, pos, ax=ax1)

    job_times = [i[len(i) - 1]for i in calculate_job_time(time,
                                                          g.topologicalSort(), G.adj._atlas)]

    labels = {}
    for i in range(len(g.topologicalSort())):
        labels[g.topologicalSort()[i]] = job_times[i]
    nx.draw(G, pos, labels=labels, with_labels=True, ax=ax2)

    plt.show()
