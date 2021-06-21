import networkx as nx
import matplotlib.pyplot as plt


def isCycle(graph):
    try:
        nx.find_cycle(graph)
        return 1
    except:
        return 0


def graph_from_edges(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G


def plot_graph(graph):
    pos = nx.spring_layout(graph)
    pos = nx.spring_layout(graph, pos=pos, fixed=graph.nodes)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap(
        'jet'), node_size=250, node_color='gray')
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, edge_color='green', arrows=True)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


a, b, c, d, e, f = 0, 1, 2, 3, 4, 5

graph = [[a, b, 2],
         [a, c, 3],
         [b, d, 3],
         [b, c, 5],
         [b, e, 4],
         [c, e, 4],
         [d, e, 2],
         [d, f, 3],
         [e, f, 5]]


def kruskals(graph: list):
    G = graph_from_edges(graph)
    plot_graph(G)
    MST = nx.Graph()
    graph.sort(key=lambda x: x[2])
    for edge in graph:
        MST.add_weighted_edges_from([edge])
        if isCycle(MST):
            plot_graph(MST)
            MST.remove_edge(edge[0], edge[1])
        plot_graph(MST)
    plot_graph(MST)


if __name__ == '__main__':
    kruskals(graph)
