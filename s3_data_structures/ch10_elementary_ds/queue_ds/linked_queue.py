from s3_data_structures.ch10_elementary_ds.queue_ds.queue import Queue
from s3_data_structures.ch10_elementary_ds.queue_ds.errors import *
from utilities.node_factory import NodeGenerator

'''
This is a queue built using linked list, so it can practically hold infinite elements.

Always establish the conditions for Queue
Tail -> always points to the last inserted element
Head -> always points to the next location to delete from
'''

class LinkedQueue(Queue):

    def __init__(self):
        super().__init__()

    def enqueue(self, x):
        '''
        Enqueue given element in the linked list
        :param x: any data object
        '''

        if self.is_empty():
            self.head = self.tail = x
        else:
            self.tail.next = x
            self.tail = self.tail.next

    def dequeue(self):
        '''
        remove the first element
        :return: removed element
        '''

        # check if queue is empty
        if self.is_empty():
            raise EmptyQueueError()

        removed_ele = self.head

        # check if its the last element in the queue
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return removed_ele

    def __str__(self):
        s = ''
        x = self.head
        while x:
            s += str(x.data) + (' => ' if x.next else '')
            x = x.next

        return s

if __name__ == '__main__':

    ng = NodeGenerator()

    n1 = ng.get_sll_node(10)
    n2 = ng.get_sll_node(20)

    lq = LinkedQueue()
    lq.enqueue(n1)

    print('Q with one element:', lq)

    try:
        ele = lq.dequeue()      # will remove the only element in theh queue
        print('Remove inserted element:', ele)

        ele = lq.dequeue()      # will throw an exception
    except EmptyQueueError as e:
        print('Error:', e.message)
        print('Suggestion:', e.suggest)
    except Error as e:
        print(e.message)

    lq.enqueue(n2)
    lq.enqueue(n1)
    print(lq)