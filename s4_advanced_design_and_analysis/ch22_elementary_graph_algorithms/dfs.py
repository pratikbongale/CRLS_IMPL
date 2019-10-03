from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import Graph
from utilities.node_factory import GraphNode
from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.bfs import print_path
from enum import Enum

class Color(Enum):
    WHITE = 1       # not visited
    GRAY = 2        # ready to be visited
    BLACK = 3       # visited

time: int = 0

def dfs(g: Graph):
    '''
    Creates a forest of depth-first trees
    DFS colors as well as timestamps every vertex v.d: discovered, v.f: finished
    :param g: an instance of class Graph
    :return:
    '''

    global time

    if not isinstance(g, Graph):
        print('invalid input, please provide an instance of Graph')
        return

    if not g.has_nodes():
        print('Please call build_graph() to initialize the graph')
        return

    for v in g.vertices.values():
        v.parent = None
        v.color = Color.WHITE

    time = 0
    for v in g.vertices.values():
        if v.color == Color.WHITE:
            dfs_visit(g, v)

def dfs_visit(g: Graph, u: GraphNode):

    global time

    time += 1
    u.d = time
    u.color = Color.GRAY

    for v in g.edges[u.data]:
        if v.color == Color.WHITE:
            v.parent = u
            dfs_visit(g, v)

    time += 1
    u.f = time
    u.color = Color.BLACK



if __name__ == '__main__':

    dir_graph = {
        '1': ['2', '4'],
        '2': ['5'],
        '3': ['5', '6'],
        '4': ['2'],
        '5': ['4'],
        '6': ['6']
    }

    undir_graph = {
        '1': ['2', '5'],
        '2': ['1', '4', '5'],
        '3': ['2', '4'],
        '4': ['2', '3', '5'],
        '5': ['1', '2', '4']
    }

    g = Graph()
    g.build_graph(dir_graph)
    g.print_graph()

    dfs(g)
    print('\nAfter DFS on directed graph, path from 1->5', end=' ')
    print_path(g, '1', '5')

    g = Graph()
    g.build_graph(undir_graph)
    g.print_graph()

    dfs(g)
    print('\nAfter BFS on undirected graph, path from 1->5', end=' ')
    print_path(g, '1', '5')