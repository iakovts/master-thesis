import tikzplotlib

import networkx as nx
import numpy as np
from collections import Counter

from networkx.drawing.nx_agraph import to_agraph

F_PATH = "../Figures/chapter1/"

edge_list = [
    ("n1", "n2"),
    ("n1", "n2"),
    ("n1", "n1"),
    ("n2", "n3"),
    ("n3", "n1"),
    ("n4", "n3"),
    ("n2", "n4"),
    ("n5", "n1"),
    ("n2", "n5"),
]

edge_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

def create_MG():
    MG = nx.MultiGraph()
    labels = edge_labels.copy()
    uniq_nodes = get_uniq_nodes()
    MG.add_nodes_from(uniq_nodes)
    c = Counter(edge_list)
    for el, times in c.items():
        lengths = np.arange(2, 6)
        if times > 1:
            l = np.random.choice(lengths, size=times, replace=False)
            for i in range(times):
                # import pdb; pdb.set_trace()
                MG.add_edge(*el, length=times, label=labels.pop(0))
        else:
            MG.add_edge(*el, label=labels.pop(0))
    return MG


def draw_graph(MG):
    A = to_agraph(MG)
    A.layout("dot")
    A.draw(F_PATH + "definition_ex_1.png")


def get_uniq_nodes():
    uniq = set()
    for el in edge_list:
        for node in el:
            uniq.add(node)
    return uniq


if __name__ == "__main__":
    MG = create_MG()
    draw_graph(MG)
