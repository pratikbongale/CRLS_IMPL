from abc import ABCMeta, abstractmethod

class MyStack:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.top = None

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def is_full(self):
        raise NotImplementedError

    @abstractmethod
    def push(self, x):
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        raise NotImplementedError