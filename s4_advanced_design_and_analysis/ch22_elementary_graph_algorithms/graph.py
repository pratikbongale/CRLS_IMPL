from abc import ABCMeta, abstractmethod
from utilities.node_factory import GraphNode
from collections import defaultdict


class Vertex:
    def __init__(self, data: str):
        self.data = data
        self.parent = None


class Graph:

    __metaclass__ = ABCMeta

    def __init__(self, adj_list=None):

        self.adj_list = defaultdict(list)

        for u in adj_list:
            u_node = GraphNode(u)
            for v in adj_list[u]:
                v_node = GraphNode(v)
                self.adj_list[u_node].append(v_node)

                if v_node not in self.adj_list:
                    self.adj_list[v_node] = []

    def print_graph(self):
        for u in self.adj_list:
            print(str(u) + ' : ', end='')
            print([str(x) for x in self.adj_list[u]], end='')
            print()

    def get_node(self, x):

        node = GraphNode(x)
        if self.adj_list and node in self.adj_list:
            return self.adj_list[node]
        else:
            return None