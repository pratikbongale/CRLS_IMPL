from collections import Counter
from itertools import accumulate
import math

def count_sort(A, B, k, key=None):
    '''
    Precondition: 0 <= A[i] <= k
    Procedure:
    -> Collect frequency
    -> Cumulative Sum(# elements before each element in 0..k)
    -> go from A.length to 1: insert elements as per index

    Features: not Inplace, Stable
    Complexity: O(n)
    '''

    if key:
        X = [key(a) for a in A]
    else:
        X = A.copy()

    ctr = Counter(X)  # returns a dictionary of elements with count
    c = list()
    for i in range(k+1):
        c.append(ctr[i])

    c = list(accumulate(c))

    for i in range(len(A)-1, -1, -1):
        B[c[X[i]]-1] = A[i]     # add -1 to ensure correct indexing
        c[X[i]] -= 1

def radix_sort(A, d):
    '''
    precondition: each element should have d-digits
    procedure:
    -> sort by last digit
    -> collect all elements
    -> sort by second to last digit
    -> collect and so on

    Features: not Inplace, Stable
    Complexity: O(n)
    '''

    # need to convert all elements to strings
    A = [str(a) for a in A]

    for i in range(d-1, -1, -1):
        A.sort(key=lambda x : int(x[i]))     # this sort is stable

    A = [int(a) for a in A]
    return A

def radix_wt_count(A, d):

    # need to convert all elements to strings
    A = [str(a) for a in A]

    for i in range(d-1, -1, -1):
        B = [0]*len(A)
        count_sort(A, B, 9, key=lambda x : int(x[i]))
        A = B.copy()

    A = [int(a) for a in A]
    return A

def bucket_sort(A):
    '''
    Assumes that input was generated from a uniform distribution
    and all inputs are equaly likely.

    Precondition: 0 <= A[i] < 1
    Procedure:
    -> create n buckets
    -> insert A[i] into B[n*A[i]] bucket (scale the value A[i])
    -> sort each bucket using insertion sort
    -> collect each bucket in order

    Features: not in-palce, stable
    Complexity: O(n)
    '''

    n = len(A)
    B = [list() for _ in range(n)]
    res = list()

    for i in range(n):
        bucket = math.floor(n*A[i])
        B[bucket].append(A[i])

    for i in range(n):
        if len(B[i]) != 0:
            res.extend(sorted(B[i]))

    return res

if __name__ ==  '__main__':
    A = [0, 1, 1, 0, 5, 0, 2, 4, 1, 4, 5]
    B = [0]*len(A)
    count_sort(A, B, k=5)
    print('Count Sort:', B)

    A = [112, 234, 423, 110, 105, 543]
    B = radix_sort(A, d=3)
    print('Radix sort:', B)

    A = [112, 234, 423, 110, 105, 543]
    B = radix_wt_count(A, d=3)
    print('Radix wt count sort:', B)

    A = [0.23, 0.45, 0.72, 0.11, 0.42, 0.18, 0.99, 0.76]
    B = bucket_sort(A)
    print('Bucket Sort:', B)



