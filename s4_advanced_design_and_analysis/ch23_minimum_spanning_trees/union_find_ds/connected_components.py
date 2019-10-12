from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import *
from s4_advanced_design_and_analysis.ch23_minimum_spanning_trees.union_find_ds.union_find_ll import UFLinkedListImpl
from typing import Hashable

def connected_components(g: Graph) -> UFLinkedListImpl:
    # stores the graph in Union-Find data structure
    # makes it each to find connected components in the graph
    # the no. of disjoint-sets in UF ds are the connected components

    uf = UFLinkedListImpl()

    for v in g.vertices:
        uf.make_set(v)

    for u in g.adj_list:
        for v in g.adj_list[u]:
            if uf.find_set(u) != uf.find_set(v):
                uf.union(u, v)

    return uf


def same_component(ds: UFLinkedListImpl, u: Hashable, v: Hashable) -> bool:
    return ds.find_set(u) == ds.find_set(v)


if __name__ == '__main__':

    undir_graph = {
        '1': ['2', '5'],
        '2': ['1', '4', '5'],
        '3': ['2', '4'],
        '4': ['2', '3', '5'],
        '5': ['1', '2', '4'],
        '6': ['6', '7']
    }

    g = Graph()
    g.build_graph(undir_graph)

    uf_ds = connected_components(g)
    print(uf_ds)

    print(same_component(uf_ds, '7', '6'))

