from abc import ABCMeta, abstractmethod
from utilities.node_factory import GraphNode
from collections import defaultdict
from typing import Dict, List, Any, DefaultDict
from enum import Enum


class Color(Enum):
    WHITE = 1       # not visited
    GRAY = 2        # added in queue, ready to be visited
    BLACK = 3       # visited, neighbors added to queue


class Graph:
    # graph with Adjacency List

    __metaclass__ = ABCMeta

    __slots__ = ['adj_list', 'vertices', 'edges']

    def __init__(self):

        self.adj_list: Dict[Any, List] = defaultdict(list)
        self.vertices: Dict[Any, GraphNode] = defaultdict(GraphNode)
        self.edges: Dict[Any, List] = defaultdict(list)

    def build_graph(self, adj_list: Dict):

        if not isinstance(adj_list, dict):
            print('Adj list must be a Dictionary object')
            return None, None

        # reset everything
        self.adj_list = defaultdict(list, adj_list)     # build default dict from existing dict
        self.vertices = defaultdict(GraphNode)
        self.edges = defaultdict(list)

        for u in adj_list:
            v1 = self.vertices[u]
            v1.data = u
            for v in adj_list[u]:
                v2 = self.vertices[v]
                v2.data = v
                self.edges[u].append(v2)

                if v not in self.edges:
                    self.edges[v] = []

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

    def is_empty(self):
        return len(self.adj_list) == 0

    def has_nodes(self):
        return not self.is_empty() and len(self.vertices) > 0

    def get_nbors(self, x):

        if self.adj_list and x in self.adj_list:
            return self.adj_list[x]
        else:
            return None