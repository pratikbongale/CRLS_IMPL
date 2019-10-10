from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import Graph, Color
from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.dfs import dfs
from typing import Any, List

'''
An application of DFS:
Decomposing a directed graph into its Strongly Connected Components 
'''

def get_scc(g: Graph):
    '''
    returns strongly connected components in given graph
    :param g: Graph object representing a directed  graph
    :return: res: List[Graph] a list of graph objects each representing a SCC
    '''

    if not isinstance(g, Graph):
        print('Not a Graph object')
        return

    # Steps:
    # 1. Compute finish times of each vertex: DFS(g)
    # 2. Compute a transpose of graph: gt
    # 3. In decreasing order of finish time(v.f), call DFS-VISIT(gt, v)
    # 4. All vertices reachable from v in gt are in the same SCC.

    dfs(g)
    gt: Graph = get_transpose(g)
    sorted_vertices: List[Any] = sorted(g.vertices, key= lambda v : g.vertices[v].f, reverse=True)

    for v in gt.vertices.values():
        v.color = Color.WHITE

    scc = dict()
    for v in sorted_vertices:
        if gt.vertices[v].color == Color.WHITE:
            reachable_v = []
            dfs_get_reachable(gt, gt.vertices[v], reachable_v)
            scc[v] = reachable_v

    return scc


def dfs_get_reachable(g, u, reachables):

    u.color = Color.GRAY
    reachables.append(u.data)

    for v in g.edges[u.data]:
        if v.color == Color.WHITE:
            dfs_get_reachable(g, v, reachables)

    u.color = Color.BLACK


def get_transpose(g):

    gt = Graph()

    # vertices remain the same
    gt.vertices = g.vertices

    # reverse the adjacency list
    # (u,v) -> (v,u)
    for u in g.adj_list:
        for v in g.adj_list[u]:
            gt.adj_list[v].append(u)
            gt.edges[v].append(gt.vertices[u])

    return gt

if __name__ == '__main__':

    adj_list = {
        'a': ['b'],
        'b': ['c', 'f', 'e'],
        'c': ['d', 'g'],
        'd': ['c', 'h'],
        'e': ['a', 'f'],
        'f': ['g'],
        'g': ['f', 'h'],
        'h': ['h']
    }

    g = Graph()
    g.build_graph(adj_list)

    print(get_scc(g))
