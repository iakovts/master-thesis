import networkx as nx
import numpy as np
from collections import Counter

from networkx.drawing.nx_agraph import to_agraph

F_PATH = "../Figures/chapter1/"

edge_list_complex = [
    (1, 2),
    (1, 2),
    (1, 1),
    (2, 3),
    (3, 1),
    (4, 3),
    (2, 4),
    (5, 1),
    (2, 5),
    (6, 2),
]
edge_list_simple = [
    (1, 2),
    (2, 3),
    (3, 1),
    (4, 3),
    (2, 4),
    (5, 1),
    (2, 5),
    (6, 2),
]

def create_simple_MG():
    el = edge_list_simple.copy()
    MG = nx.MultiGraph(edge_list_simple)
    return MG

def create_complex_MG():
    el = edge_list_complex.copy()
    MG = nx.MultiGraph(edge_list_complex)
    return MG
        
def draw_graph(MG, name):
    A = to_agraph(MG)
    A.layout("dot")
    A.draw(F_PATH + name)


if __name__ == "__main__":
    MG_S = create_simple_MG()
    MG_C = create_complex_MG()
    draw_graph(MG_S, "simple_graph_adj.png")
    draw_graph(MG_C, "complex_graph_adj.png")
