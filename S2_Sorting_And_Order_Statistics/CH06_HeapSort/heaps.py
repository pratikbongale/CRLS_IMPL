def left(i):
    return 2*i+1

def right(i):
    return (2*i)+2

def max_heapify(A, i, heapsize):

    # heap-down
    # assumes left and right subtrees are heaps
    # but A[i] may be violating the heap property
    # always keep in mind the HEAPSIZE property
    # it tells which are valid elements of the heap

    largest = i
    l = left(i)
    r = right(i)
    if l < heapsize and A[l] > A[largest]:
        largest = l

    if r < heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest, heapsize)

def build_max_heap(A):

    mid = len(A) // 2
    heapsize = len(A)
    for i in range(mid, -1, -1):
        # all elements after the mid ele will be leaf nodes
        max_heapify(A, i, heapsize)

def heap_sort(A):

    build_max_heap(A)       # O(nlogn)
    heapsize = len(A)
    for i in range(len(A)-1, -1, -1):
        A[i], A[0] = A[0], A[i]
        heapsize -= 1
        max_heapify(A, 0, heapsize)

# class Heap:
#     def __init__(self, A):
#         self.A = A
#         self.heapsize = 0


if __name__ == '__main__':

    A = [5, 1, 4, -2, 9, -5]

    # h = Heap(A)

    heap_sort(A)
    print(A)