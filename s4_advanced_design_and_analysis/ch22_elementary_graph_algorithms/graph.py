from enum import Enum
from abc import ABCMeta, abstractmethod

class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3

class Vertex:
    def __init__(self, data:str):
        self.data = data
        self.parent = None

class Graph:

    __metaclass__ = ABCMeta

    @abstractmethod
    def insert_edge(self, u, v):
        raise NotImplementedError

    def __init__(self):
        self.adj_list = dict()

    def print_graph(self):
        pass

