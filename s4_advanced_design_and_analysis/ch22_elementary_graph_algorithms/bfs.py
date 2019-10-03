from enum import Enum
from s3_data_structures.ch10_elementary_ds.queue_ds.linked_queue import LinkedQueue
from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import *
import math


class Color(Enum):
    WHITE = 1       # not visited
    GRAY = 2        # added in queue, ready to be visited
    BLACK = 3       # visited, neighbors added to queue


def bfs(g: Graph, s: Any):
    """
    Primarily used to find the shortest distance of all nodes from a given start node 's'
    Note: This method create a single BFS tree, connecting all nodes in subgraph(g) which contains 's'
    :param g: adjacency list representation of graph
    :param s: start node
    """

    if len(g.adj_list) > 0:
        if s not in g.adj_list:
            print('Start node not found in graph')
            return
    else:
        print('Graph not initialized, please call build_graph()')
        return

    # convert all elements to nodes
    # color all nodes white
    for v in g.vertices.values():
        v.color = Color.WHITE
        v.dist = math.inf
        v.parent = None

    s_node = g.vertices[s]
    s_node.color = Color.GRAY
    s_node.dist = 0
    s_node.parent = None

    q = LinkedQueue()
    q.enqueue(s_node)

    while not q.is_empty():
        u: GraphNode = q.dequeue()

        for v in g.edges[u.data]:

            if v.color == Color.WHITE:  # not visited
                v.color = Color.GRAY    # visit this node
                v.dist = u.dist + 1
                v.parent = u
                q.enqueue(v)

        u.color = Color.BLACK   # done processing this node


def print_path(g: Graph, s: Any, t:Any):

    s_node = g.vertices[s]
    t_node = g.vertices[t]

    if t_node == s_node:
        print(str(s), end=' ')
    elif t_node.parent is None:
        print('No path from', s, 'to', t)
    else:
        print_path(g, s, t_node.parent.data)
        print(str(t), end=' ')


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

    bfs(g, '1')
    print('\nAfter BFS on directed graph, path from 1->5', end=' ')
    print_path(g, '1', '5')

    g = Graph()
    g.build_graph(undir_graph)
    g.print_graph()

    bfs(g, '1')
    print('\nAfter BFS on undirected graph, path from 1->5', end=' ')
    print_path(g, '1', '5')