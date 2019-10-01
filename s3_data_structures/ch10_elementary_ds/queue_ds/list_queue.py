from s3_data_structures.ch10_elementary_ds.queue_ds.my_queue import MyQueue
from s3_data_structures.ch10_elementary_ds.queue_ds.errors import *
from typing import List, Any

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


class ListQueue(MyQueue):

    def __init__(self, length: int = 10) -> None:
        super().__init__()

        self.q_size: int = length
        self.head: int = 0       # here head is an index
        self.tail: int = 0       # here tail is an index
        self.q: List[Any] = [None] * length

    def is_full(self):
        return (self.tail + 1) % self.q_size == self.head

    def is_empty(self):
        return self.head == self.tail

    def enqueue(self, x: Any) -> None:
        '''
        Enqueue given element in the linked list
        '''

        if self.is_full():
            raise FullQueueError

        self.q[self.tail] = x
        self.tail = self.tail + 1

        if self.tail == self.q_size:
            self.tail = 0

    def dequeue(self) -> Any:
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

    def __str__(self) -> str:
        s: str = ''

        if self.is_empty():
            s += 'Empty'
            return s

        i: int = self.head

        while i != self.tail:

            s += str(self.q[i]) + ' => '
            i += 1

            if i == self.q_size:
                i = 0

        s += str(self.q[i])     # print the element pointed by tail_idx

        return s


class DynamicListQueue(ListQueue):

    def __init__(self):
        super().__init__(length=10)
        self.threshold: float = 0.9
        self.q_length: int = 0

    def enqueue(self, x: Any) -> None:

        # check if queue is filled upto threshold
        if self.q_length >= int(self.q_size * self.threshold):

            # move all elements from current arr to a larger arr
            # or we can just add more memory to current arr
            self.q.extend([None]*self.q_length)      # double the size
            self.q_size += self.q_length

        try:
            super().enqueue(x)
            self.q_length += 1      # increase length if exception not raised
        except FullQueueError as err:
            print(err.message)


if __name__ == '__main__':

    # test static queue (fixed length)
    print('test static queue (fixed length)')
    queue_length = 5
    q = ListQueue(queue_length)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

    try:
        q.enqueue(50)
    except FullQueueError as e:
        print(e.message)

    print(q)

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    print(q)

    try:
        q.dequeue()
    except EmptyQueueError as e:
        print(e.message)

    # test dynamic queue (dynamic length)')
    print('Test dynamic queue (dynamic length)')
    dyn_lq = DynamicListQueue()

    for i in range(15):
        dyn_lq.enqueue(i+1)

    print(dyn_lq)

    for i in range(16):
        try:
            print('Removed:', dyn_lq.dequeue())
        except EmptyQueueError as e:
            print(e.message)
