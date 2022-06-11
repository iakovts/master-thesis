import networkx as nx
import numpy as np

from networkx.drawing.nx_agraph import to_agraph

F_PATH = "../Figures/chapter1/"

edge_list = [
    ("s1", "s2"),
    ("s2", "s3"),
    ("s3", "s1"),
    ("s4", "s3"),
    ("s2", "s4"),
    ("s5", "s1"),
    ("s2", "s5"),
]

edge_labels = ["A", "B", "C", "D", "E", "F", "G"]

def create_MG():
    G = nx.Graph()
    uniq_nodes = get_uniq_nodes()
    G.add_nodes_from(uniq_nodes)
    for el in edge_list:
        G.add_edge(*el, label=edge_labels.pop(0))

    return G
        
        

def get_uniq_nodes():
    uniq = set()
    for el in edge_list:
        for node in el:
            uniq.add(node)
    return uniq

def draw_graph(MG, fname):
    A = to_agraph(MG)
    A.layout("dot")
    A.draw(F_PATH + fname)

if __name__ == "__main__":
    G = create_MG()
    draw_graph(G, "example_node_properties.png")
    A = nx.to_numpy_array(G)
    np.savetxt("A_properties.txt", A, fmt="%1d", delimiter="\t")
