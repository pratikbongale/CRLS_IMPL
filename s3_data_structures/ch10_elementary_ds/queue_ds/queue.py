from abc import ABCMeta, abstractmethod

class Queue:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.head = None
        self.tail = None

    @abstractmethod
    def enqueue(self, x):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError

    def is_empty(self):
        return self.head is None


'''
Below is the simple implementation of queue from CRLS
'''
head = tail = 0

def enqueue(Q, x):
    global tail

    if is_full(Q):
        return 'Queue is full'
    else:
        Q[tail] = x
        tail = tail + 1

        if tail == len(Q):
            tail = 0

def dequeue(Q):
    global head
    if is_empty(Q):
        return 'Queue is empty'
    else:
        res = Q[head]
        head = head + 1

        if head == len(Q):
            head = 0

        return res

def is_full(Q):
    return tail+1 == head

def is_empty(Q):
    return head == tail


if __name__ == '__main__':
    queue_length = 5
    Q = [0] * queue_length

    enqueue(Q, 10)
    enqueue(Q, 20)
    enqueue(Q, 30)
    print(Q)

    print(dequeue(Q))
    enqueue(Q,40)
    print(Q)

    print(dequeue(Q))
    print(dequeue(Q))
    print(dequeue(Q))
    print(dequeue(Q))



