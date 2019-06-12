from abc import ABCMeta, abstractmethod

class HashTable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, x):
        raise NotImplementedError

    @abstractmethod
    def delete(self, x):
        raise NotImplementedError

    @abstractmethod
    def search(self, key):
        raise NotImplementedError
