import math
from s2_sorting_and_order_statistics.ch06_heap_sort.heaps import max_heapify
from s2_sorting_and_order_statistics.ch06_heap_sort.heaps import build_max_heap

def maximum(A):
    return A[0]

def extract_maximum(A, heapsize):
    # find and remove the maximum element
    if len(A) < 1:
        return None

    res = maximum(A)

    last_i = heapsize-1
    A[0] = A[last_i]
    heapsize -= 1
    max_heapify(A, 0, heapsize)

    return res

def parent(i):

    if i % 2 == 0:
        return (i // 2) - 1
    else:
        return i // 2

def heap_increase_key(A, i, new_key):
    # increase the priority at index i
    # assumes that new_key is greater than existing ket at A[i]

    if new_key < A[i]:
        return None

    A[i] = new_key
    while i > 0 and A[i] > A[parent(i)]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def max_heap_insert(A, key, heapsize):
    heapsize = heapsize + 1
    A.append(None)
    A[heapsize-1] = -math.inf     # insert at the last position
    heap_increase_key(A, heapsize-1, key)

if __name__ == '__main__':

    A = [5, 1, 4, -2, 9, -5]

    build_max_heap(A)
    m = extract_maximum(A, heapsize=len(A))
    print(m)
    max_heap_insert(A, key=10, heapsize=len(A))
    print(maximum(A))

