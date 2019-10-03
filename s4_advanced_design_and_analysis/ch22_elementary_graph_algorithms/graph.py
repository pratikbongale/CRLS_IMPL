from abc import ABCMeta, abstractmethod
from utilities.node_factory import GraphNode
from collections import defaultdict
from typing import Dict, List, Any, DefaultDict


class Vertex:
    def __init__(self, data: str):
        self.data = data
        self.parent = None


class Graph:
    # graph with Adjacency List

    __metaclass__ = ABCMeta

    def __init__(self):

        self.adj_list: Dict[Any, List] = defaultdict(list)
        self.vertices: Dict[Any, GraphNode] = defaultdict(GraphNode)
        self.edges: Dict[Any, List] = defaultdict(list)

    def build_graph(self, adj_list: Dict):

        if isinstance(adj_list, dict):
            self.adj_list = adj_list

        for u in adj_list:
            v1 = self.vertices[u]
            v1.data = u
            for v in adj_list[u]:
                v2 = self.vertices[v]
                self.edges[u].append(v2)

        return self.vertices, self.edges

    def print_graph(self):
        print()
        for u in self.adj_list:
            print(str(u) + ' : ', end='')
            print([str(x) for x in self.adj_list[u]], end='')
            print()

    def get_vertex(self, x):
        if x in self.vertices:
            return self.vertices[x]
        else:
            print('Node not found in graph')
            return None

    def get_nbors(self, x):

        if self.adj_list and x in self.adj_list:
            return self.adj_list[x]
        else:
            return None