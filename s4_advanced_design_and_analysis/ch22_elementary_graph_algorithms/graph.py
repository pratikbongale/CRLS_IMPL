from abc import ABCMeta, abstractmethod
from utilities.node_factory import GraphNode
from collections import defaultdict
from typing import Dict


class Vertex:
    def __init__(self, data: str):
        self.data = data
        self.parent = None


class Graph:
    # graph with Adjacency List

    __metaclass__ = ABCMeta

    def __init__(self):

        self.adj_list: Dict = defaultdict(list)

    def build_graph(self, adj_list: Dict):

        if isinstance(adj_list, dict):
            self.adj_list = adj_list

        # for u in adj_list:
        #     u_node = GraphNode(u)  # fails here, GraphNode is mutable (unhashable)
        #     for v in adj_list[u]:
        #         v_node = GraphNode(v)
        #         self.adj_list[u_node].append(v_node)
        #
        #         if v_node not in self.adj_list:
        #             self.adj_list[v_node] = []

    def print_graph(self):
        for u in self.adj_list:
            print(str(u) + ' : ', end='')
            print([str(x) for x in self.adj_list[u]], end='')
            print()

    def get_nbors(self, x):

        if self.adj_list and x in self.adj_list:
            return self.adj_list[x]
        else:
            return None