import networkx as nx
import numpy as np

from networkx.drawing.nx_agraph import to_agraph

F_PATH = "../Figures/chapter1/"
edge_list = [(1, 2), (1, 2), (2, 3), (3, 1)]
# node_list =  [1, 2, 3]
edge_labels  = [0.5, 1.2, 3, 1]


def create_MG():

    MG = nx.MultiGraph()
    for el in edge_list:
        MG.add_edge(*el, label=edge_labels.pop())
    return MG
        
def draw_graph(MG, name):
    A = to_agraph(MG)
    A.layout("dot")
    A.draw(F_PATH + name)

if __name__ == "__main__":
    MG = create_MG()
    draw_graph(MG, "simple_weighted.png")
