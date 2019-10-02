from enum import Enum
from s3_data_structures.ch10_elementary_ds.queue_ds.linked_queue import LinkedQueue
from s4_advanced_design_and_analysis.ch22_elementary_graph_algorithms.graph import *
from utilities.node_factory import GraphNode
import math



class Color(Enum):
    WHITE = 1       # not visited
    GRAY = 2        # added in queue, ready to be visited
    BLACK = 3       # visited, neighbors added to queue


def bfs(g, s):
    """
    Primarily used to find the shortest distance of all nodes from a given start node
    :param g: adjacency list representation of graph
    :param s: start node
    """

    if s not in g.adj_list:
        print('Start node not found in graph')
        return

    bfs_graph = Graph()
    bfs_graph.v_map = dict()

    # convert all elements to nodes
    # color all nodes white
    for u in g.adj_list.keys():
        n = GraphNode(u)     # create graph node
        n.color = Color.WHITE
        n.dist = math.inf
        n.parent = None

        bfs_graph.v_map[u] = n   # store in vertex map

    s = bfs_graph.v_map[s]
    s.color = Color.GRAY
    s.dist = 0
    s.parent = None

    q = LinkedQueue()
    q.enqueue(s)

    while not q.is_empty():
        u = q.dequeue()

        for v in g.adj_list[u.data]:

            v = bfs_graph.v_map[v]  # get a bfs node of this element

            if v.color == Color.WHITE:
                # not visited
                v.color = Color.GRAY  # visit this node
                v.dist = u.dist + 1
                v.parent = u
                q.enqueue(v)

        u.color = Color.BLACK   # done processing this node

    return bfs_graph

def print_path(g, s, t):

    t_node = g.v_map[t]

    if t == s:
        print(str(s))
    elif t_node.parent is None:
        print('No path')
    else:
        print_path(g, s, t_node.parent)


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
    print('\nNeighbors of 1:', g.get_nbors('1'))

    bfs_graph = bfs(g, '1')
    print_path(bfs_graph, '1', '5')     # TODO: fix needed










