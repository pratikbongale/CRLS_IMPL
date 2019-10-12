from abc import ABCMeta, abstractmethod
from utilities.node_factory import Node

class LinkedList:

    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, x):
        raise NotImplementedError

    @abstractmethod
    def remove_ele(self, x):
        raise NotImplementedError

    @abstractmethod
    def print_list(self):
        raise NotImplementedError