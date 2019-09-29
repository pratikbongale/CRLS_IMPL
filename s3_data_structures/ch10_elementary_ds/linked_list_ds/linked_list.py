from abc import ABCMeta, abstractmethod
from utilities.error import Error


class LinkedList:

    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, x):
        raise NotImplementedError

    @abstractmethod
    def remove_ele(self, x):
        raise NotImplementedError

    @abstractmethod
    def pritn_list(self):
        raise NotImplementedError