import sys
import configargparse
import networkx as nx
import numpy as np
sys.path.append("./src")
from plotter import show_graph, show_NN
from utils import mat2graph, gen_NN

def parse_args():
    p = configargparse.ArgParser(default_config_files=['./default.conf'])
    p.add('-c', '--my-config', required=True, is_config_file=True, help='config file path')
    p.add('-net', '--network', default='16module', help='Chose network from [4module, 16module, 64module, 64hilbert]')
    p.add('-m', '--mode', default='graph', help='Chose mode from [graph, neuron]')
    p.add('--cd', default=1000, type=int, help='cell density (/mm2)')
    p.add('--pin', default=0.5, type=float, help='intramodule connection probability')
    p.add('--pout', default=0.1, type=float, help='intermodule connection probability')
    return p.parse_args()

def main():
    args = parse_args()
    adj_mat = np.loadtxt("./network/" + args.network + ".csv", delimiter=",") #4module.csv, 16module.csv, 64module.csv, 64hilbert.csv
    if args.mode == 'graph':
        G, pos = mat2graph(np.array(adj_mat))
        show_graph(G, pos)
    elif args.mode == 'neuron':
        G, pos = gen_NN(args.cd, adj_mat, pin=args.pin, pout=args.pout)
        show_NN(G, pos)

    print("Average path lengs:", nx.average_shortest_path_length(G))
    print("Average clustering:", nx.average_clustering(G))

if __name__ == '__main__':
    main()