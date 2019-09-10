from s3_data_structures.ch10_elementary_ds.queue_ds.queue import Queue
from s3_data_structures.ch10_elementary_ds.queue_ds.errors import *
from utilities.node_factory import NodeGenerator

'''
This is a fixed length queue

Always establish the conditions for Queue
Tail -> always points to the next location to insert
Head -> always points to the next location to delete from (except when q is empty)

Q is initial when head = tail = -1
Q is full when tail + 1 = head
Q is empty when head = tail
Q can store N-1 elements only  

Why only N-1 elements:
+++ If we try to store N elements our conditions tail+1 == head will be true
    when queue is empty as well as queue is full
    [0,1,2,3,4,5]  tail = 5, head = 0  FULL
    [0,1,2,3,4,5]  tail = 3, head = 3  One element in Q (t=3, h=3)
    [0,1,2,3,4,5]  tail = 3, head = 4  EMPTY  (after deleting that one element) 
'''

class ListQueue(Queue):

    def __init__(self, length=10):
        super().__init__()
        self.q_size = length
        self.head = 0
        self.tail = 0
        self.q = [None] * length

    def is_full(self):
        return self.tail + 1 == self.head

    def enqueue(self, x):
        '''
        Enqueue given element in the linked list
        :param x: any data object
        '''

        if self.is_full():
            raise FullQueueError

        self.q[self.tail] = x
        self.tail = self.tail + 1

        if self.tail == self.q_size:
            self.tail = 0

    def dequeue(self):
        '''
        remove the element pointed to by head
        :return: removed element
        '''

        if self.is_empty():
            raise EmptyQueueError()

        removed_ele = self.q[self.head]
        self.head = self.head + 1

        if self.head == self.q_size:
            self.head = 0

        return removed_ele

    def __str__(self):
        s = ''
        x = self.head
        while x:
            s += str(x.data) + (' => ' if x.next else '')
            x = x.next

        return s