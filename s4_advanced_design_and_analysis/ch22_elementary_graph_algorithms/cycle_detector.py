from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import Graph, Color, GraphNode
from typing import List, Dict, Any, Set

WHITE = 0
GRAY = 1
BLACK = 3

ENTER = 0
EXIT = 1


def is_cyclic_stack(g: Graph):
    '''
    Finds if g contains a cycle
    :param g: Graph
    :return: Boolean value indicating if a cycle exists in g
    '''

    if not isinstance(g, Graph):
        print('Not a graph object')

    # method 1: iterative dfs (did not work)
    # maintain elements in stack in another set, such that all elements in stack must also be in the set
    # maintain a visited set

    # method 2: recursive dfs (Geeks for Geeks)
    # map each vertex of graph to an integer index
    # then maintain rec_stack = [False] * len(V)
    # and maintain visited = [False] * len(V)
    # write a recursive dfs program

    # method 3: maintain colors and state of each vertex
    # push each vertex twice into the stack

    state = {v: WHITE for v in g.vertices}
    stack = []

    for v in g.vertices:
        if state[v] is not BLACK:
            if dfs_visit_stack(g, v, state, stack) == True:
                return True

    return False


def dfs_visit_stack(g, start, state, stack):

    stack.append((ENTER, start))

    while stack:
        act, v = stack.pop()

        if act == EXIT:
            # print('Exit', v)
            state[v] = BLACK

        else: # act == ENTER

            # print('Enter', v)
            stack.append((EXIT, v))
            state[v] = GRAY     # only set GRAY when you pop v -> (start processing v)

            for n in g.adj_list[v]:
                if state[n] == GRAY:
                    # print('Found cycle at', n)
                    return True
                elif state[n] == WHITE:
                    stack.append((ENTER, n))

    return False


def is_cyclic_color(g: Graph):

    if not isinstance(g, Graph):
        print('Not a graph object')
        return False

    for v in g.vertices.values():
        v.color = Color.WHITE
        v.parent = None
        v.d = 0
        v.f = 0

    for v in g.vertices.values():
        if v.color == Color.WHITE and dfs_visit_color(g, v) == True:
            return True     # found a cycle

    return False    # not cyclic

time = 0

def dfs_visit_color(g: Graph, u: GraphNode):

    global time

    time += 1
    u.color = Color.GRAY
    u.d = time

    for v in g.edges[u.data]:
        if v.color == Color.WHITE:
            v.parent = u
            if dfs_visit_color(g, v):
                return True
        elif v.color == Color.GRAY:
            return True

    time += 1
    u.color = Color.BLACK
    u.f = time

    return False

if __name__ == '__main__':

    # input must be a directed graph
    dir_graph_cyc = {
        '1': ['2', '4'],
        '2': ['5'],
        '3': ['5', '6'],
        '4': ['2'],
        '5': ['4'],
        '6': ['6']
    }

    dir_graph_acyc = {
        '1': ['2', '3'],
        '2': ['4'],
        '3': ['4']
    }

    g = Graph()
    g.build_graph(dir_graph_cyc)
    print(is_cyclic_color(g))       # TRUE

    g = Graph()
    g.build_graph(dir_graph_acyc)
    print(is_cyclic_color(g))       # FALSE

    g = Graph()
    g.build_graph(dir_graph_cyc)
    print(is_cyclic_stack(g))       # TRUE

    g = Graph()
    g.build_graph(dir_graph_acyc)
    print(is_cyclic_stack(g))