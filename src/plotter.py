import networkx as nx
import matplotlib.pyplot as plt

def show_graph(gr, pos):
    plt.figure(figsize=(5,5))
    n = gr.number_of_nodes()
    nx.draw(gr, pos, node_size=10**4//n, node_shape="s", node_color="k", edge_color="k", width=2)
    plt.show()

def show_NN(G, pos):
    plt.figure(figsize=(5,5))
    n = G.number_of_nodes()
    nx.draw_networkx(G, pos, node_size=10**4//n, node_color="grey", edge_color="k", width=.5, with_labels=False)
    plt.show()
