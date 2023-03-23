import numpy as np
import networkx as nx

def mat2graph(adjacency_matrix):
    rows, cols = np.where(adjacency_matrix != 0)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    all_rows = range(0, adjacency_matrix.shape[0])
    for n in all_rows:
        gr.add_node(n)
    gr.add_edges_from(edges)
    pos={}
    k = 0
    n = int(np.sqrt(len(adjacency_matrix)))
    for i in range(n):
        for j in range(n):
            pos[k] = (i, j)
            k += 1
    return gr, pos

def list2mat(graph):
    n = len(graph)
    graph_new = np.zeros((n,n)) 
    for i, g_i in enumerate(graph):
        for j in g_i:
            graph_new[i][j] = 1
    return graph_new

def gen_NN(cd, graph, pin=0.5, pout=0.1):
    m = len(graph)
    n = int(cd*m*0.01)
    sizes = np.array(np.ones(m)*n/m, dtype='int')
    probs = graph*pout + pin*np.diag(np.ones(m))
    G = nx.generators.community.stochastic_block_model(sizes, probs, directed=False, selfloops=False)
    pos={}
    XY = np.random.rand(n,2)
    for i in range(n):
        pos[i] = (100*XY[i,0]+200*((i//(n/m))//np.sqrt(m)), 100*XY[i,1]+200*((i//(n/m))%np.sqrt(m)))
    return G, pos