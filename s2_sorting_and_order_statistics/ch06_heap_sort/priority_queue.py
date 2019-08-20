import math
from s2_sorting_and_order_statistics.ch06_heap_sort.heaps import MaxHeap, MinHeap


class MaxPriorityQueue(MaxHeap):

    def __init__(self, arr, initial_val=-math.inf):
        super().__init__(arr)
        self.initial_val = initial_val

    def maximum(self):
        # get the max value(root node's value)
        if self.A:
            return self.A[0]
        else:
            return None

    def extract_maximum(self):
        # find and remove the maximum element
        if len(self.A) < 1:
            return None

        res = self.maximum()

        last_i = self.heapsize-1    # last_index

        self.A[0] = self.A[last_i]
        self.heapsize -= 1
        self.max_heapify(0)

        return res

    def heap_increase_key(self, i, new_key):
        # increase the priority at index i
        # assumes that new_key is greater than existing ket at A[i]

        # helper function to compute parent index
        def parent(i):
            return (i//2) - 1 if i % 2 == 0 else i//2

        if new_key > self.A[i]:
            self.A[i] = new_key
            while i > 0 and self.A[i] > self.A[parent(i)]:
                self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
                i = parent(i)

    def max_heap_insert(self, new_key):
        self.heapsize += 1
        last_i = self.heapsize-1

        if last_i < len(self.A):
            self.A[last_i] = self.initial_val  # insert at the last position
        else:
            self.A.append(self.initial_val)  # insert at the last position

        self.heap_increase_key(last_i, new_key)

class MinPriorityQueue(MinHeap):

    def __init__(self, arr, initial_val=math.inf):
        super().__init__(arr)
        self.initial_val = initial_val

    def minimum(self):
        # get the max value(root node's value)
        if self.A:
            return self.A[0]
        else:
            return None

    def extract_minimum(self):
        # find and remove the maximum element
        if len(self.A) < 1:
            return None

        res = self.minimum()

        last_i = self.heapsize-1    # last_index

        self.A[0] = self.A[last_i]
        self.heapsize -= 1
        self.min_heapify(0)

        return res

    def heap_decrease_key(self, i, new_key):
        # decrease the priority at index i
        # assumes that new_key is smaller than existing key at A[i]

        # helper function to compute parent index
        def parent(i):
            return (i//2) - 1 if i % 2 == 0 else i//2

        if new_key < self.A[i]:
            self.A[i] = new_key
            while i > 0 and self.A[i] < self.A[parent(i)]:
                self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
                i = parent(i)

    def min_heap_insert(self, new_key):
        self.heapsize += 1
        last_i = self.heapsize-1

        if last_i < len(self.A):
            self.A[last_i] = self.initial_val  # insert at the last position
        else:
            self.A.append(self.initial_val)  # insert at the last position

        self.heap_decrease_key(last_i, new_key)

if __name__ == '__main__':

    # test max priority queue
    arr = [5, 1, 4, -2, 9, -5]
    max_pq = MaxPriorityQueue(arr)

    m = max_pq.extract_maximum()
    print(m)
    max_pq.max_heap_insert(10)
    print(max_pq.maximum())

    # test min priority queue
    arr = [5, 1, 4, -2, 9, -5]
    min_pq = MinPriorityQueue(arr)

    m = min_pq.extract_minimum()
    print(m)
    min_pq.min_heap_insert(-8)
    print(min_pq.minimum())
