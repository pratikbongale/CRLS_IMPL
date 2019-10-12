from typing import Any
from abc import ABCMeta, abstractmethod

class UnionFind:

    __metaclass__ = ABCMeta

    @abstractmethod
    def make_set(self, x: Any):
        raise NotImplementedError

    @abstractmethod
    def find_set(self, x: Any):
        raise NotImplementedError

    @abstractmethod
    def union(self, s1, s2):
        raise NotImplementedError