def max_heap_sort(arr):
    # uses max heap

    mxh = MaxHeap(arr)

    for i in range(len(mxh.A)-1, -1, -1):

        # move the largest element(A[0]) to the end of array
        mxh.A[0], mxh.A[i] = mxh.A[i], mxh.A[0]

        # reduce heap size so that recently moved element is not touched
        mxh.heapsize -= 1

        # fix the tree such that largest element is again at the top
        mxh.max_heapify(0)

    return mxh.A


def min_heap_sort(arr):
    # uses min heap

    mnh = MinHeap(arr)

    for i in range(len(mnh.A)-1, -1, -1):

        # move the smallest element(A[0]) to the end of array
        mnh.A[0], mnh.A[i] = mnh.A[i], mnh.A[0]

        # reduce heap size so that recently moved element is not touched
        mnh.heapsize -= 1

        # fix the tree such that largest element is again at the top
        mnh.min_heapify(0)

    return mnh.A


class MaxHeap:
    # heapsize: number of elements currently in the heap.

    def __init__(self, arr):
        self.heapsize = len(arr)
        self.A = arr
        self.build_max_heap() # converts arr into a heap and stores it

    def build_max_heap(self):
        mid = len(self.A) // 2
        for i in range(mid, -1, -1):
            # all elements after the mid ele will be leaf nodes
            self.max_heapify(i)

    def max_heapify(self, i):

        # heap-down
        # assumes left and right subtrees are heaps
        # but A[i] may be violating the heap property
        # always keep in mind the HEAPSIZE property
        # it tells which are valid elements of the heap

        largest = i
        l = self.left(i)
        r = self.right(i)
        if l < self.heapsize and self.A[l] > self.A[largest]:
            largest = l

        if r < self.heapsize and self.A[r] > self.A[largest]:
            largest = r

        if largest != i:
            self.A[largest], self.A[i] = self.A[i], self.A[largest]
            self.max_heapify(largest)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

class MinHeap:
    def __init__(self, arr):
        self.heapsize = len(arr)
        self.A = arr
        self.build_min_heap() # converts arr into a heap and stores it

    def build_min_heap(self):
        mid = len(self.A) // 2
        for i in range(mid, -1, -1):
            # all elements after the mid ele will be leaf nodes
            self.min_heapify(i)

    def min_heapify(self, i):

        # heap-down
        # assumes left and right subtrees are heaps
        # but A[i] may be violating the heap property
        # always keep in mind the HEAPSIZE property
        # it tells which are valid elements of the heap

        smallest = i
        l = self.left(i)
        r = self.right(i)
        if l < self.heapsize and self.A[l] < self.A[smallest]:
            smallest = l

        if r < self.heapsize and self.A[r] < self.A[smallest]:
            smallest = r

        if smallest != i:
            self.A[smallest], self.A[i] = self.A[i], self.A[smallest]
            self.min_heapify(smallest)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

if __name__ == '__main__':

    A = [5, 1, 4, -2, 9, -5]

    h = max_heap_sort(A)
    print(h)

    h = min_heap_sort(A)
    print(h)