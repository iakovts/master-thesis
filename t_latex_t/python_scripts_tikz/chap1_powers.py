import networkx as nx
import numpy as np

from networkx.drawing.nx_agraph import to_agraph

F_PATH = "../Figures/chapter1/"
edge_list_s2 = [
    (1, 2),
    (2, 3),
    (1, 3),
    (2, 4),
    (1, 5),
    (2, 5),
    (4, 6),
]
        
def create_simple_MG():
    el = edge_list_s2.copy()
    MG = nx.MultiGraph(edge_list_s2)
    return MG

def draw_graph(MG, name):
    A = to_agraph(MG)
    A.layout("dot")
    A.draw(F_PATH + name)


if __name__ == "__main__":
    MG = create_simple_MG()
    draw_graph(MG, "simple_graph_dist.png")
