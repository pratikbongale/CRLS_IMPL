from enum import Enum
from s3_data_structures.ch10_elementary_ds.queue_ds.linked_queue import LinkedQueue
from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import *
import math


class Color(Enum):
    WHITE = 1       # not visited
    GRAY = 2        # added in queue, ready to be visited
    BLACK = 3       # visited, neighbors added to queue


def bfs(graph, s):
    """
    Primarily used to find the shortest distance of all nodes from a given start node
    :param graph: adjacency list representation of graph
    :param s: start node
    """

    # color all nodes to be white
    for u in graph.adj_list:
        u.color = Color.WHITE
        u.dist = math.inf
        u.parent = None

    s.color = Color.GRAY
    s.dist = 0
    s.parent = None

    q = LinkedQueue()
    q.enqueue(s)

    while not q.is_empty():
        u = q.dequeue()

        for v in graph.adj[u]:
            if v.color == Color.WHITE:
                # not visited
                v.color = Color.GRAY  # visit this node
                v.dist = u.dist + 1
                v.parent = u
                q.enqueue(v)

        u.color = Color.BLACK   # done processing this node


def print_path(s, t):

    if t == s:
        print(str(s))
    elif t.parent is None:
        print('No path')
    else:
        print_path(s, t.parent)


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

    g = Graph(dir_graph)
    g.print_graph()
    print(g.get_node('1'))







