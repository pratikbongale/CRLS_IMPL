from abc import ABCMeta, abstractmethod


class MyQueue:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.head = None
        self.tail = None

    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def is_full(self):
        raise NotImplementedError

    @abstractmethod
    def enqueue(self, x):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError