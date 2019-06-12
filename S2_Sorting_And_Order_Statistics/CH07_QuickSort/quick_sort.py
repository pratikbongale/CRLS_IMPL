import random
from S1_Foundations.CH02_BasicSorts.insertion_sort import insertion_sort_inplace

'''
QUICK SORT
- fast in-place sorting algorithm
- expected running time = O(nlgn)

Has troubles when array is sorted(asc/desc) or all elements are the same
- Solution: use the randomized version 
'''

def simple_quicksort(A, p, r):
    # we pass start index and end index because we are going to make this recursive

    if p < r:
        q = partition(A, p, r)
        simple_quicksort(A, p, q-1)
        simple_quicksort(A, q+1, r)


def partition(A, p, r, piv=None):
    '''
    Choose last element as pivot(x) and shuffle the array such that
    x is its the final sorted position.

    piv: if given is the index of pivot element
    '''

    if piv:
        x = A[piv]
    else:
        x = A[r]

    i = p-1         # tracks position of last insert

    # loop should go from p upto position (r-1)
    for j in range(p, r):     # points to next unclassified element
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]   # put the pivot element in its rightful place

    return i+1      # return the pivot idx for further partitioning


def randomized_quicksort(A, p, r):
    '''
    only the partition function is modified
    we now choose pivot at random

    to increase the randomness, we can select 3 random indices
    and then take the median of those indices
    '''

    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)

def randomized_partition(A, p, r):
    # only finding the pivot part is changed

    piv = random.randint(p, r)
    A[piv], A[r] = A[r], A[piv]     # put the pivot element in last position

    return partition(A, p, r)

def quick_ins_sort(A, p, r, k):
    '''
    Improve quick sort by using faster insertion sort when you
    have the input almost sorted.

    How: when less than k elements are left in subarray, return
    the subarray unsorted. when the topmost call returns,
    sort the whole array using insertion sort.

    Complexity: O(nk + nlg(n/k))
    '''

    if p < r and (r-p+1) >= k:
        q = partition(A, p, r)
        quick_ins_sort(A, p, q-1, k)
        quick_ins_sort(A, q+1, r, k)


def partition_all_eq(A, p, r):
    '''
    When all elements are equal, all above methods fail.
    Solution:
    - use one more partition of array [ <x | =x | >x ]
    - return 2 indices q and t such that p <= q <= t <= r
    - keep in mind that partition process must take O(r-p+1)
    '''

    x = A[r]
    i = t = p-1

    for j in range(p, r):
        if A[j] < x:

            if i < t:
                t += 1
                A[j], A[t] = A[t], A[j]
                i += 1
                A[t], A[i] = A[i], A[t]
            else:
                # i == t
                t += 1
                i += 1
                A[j], A[i] = A[i], A[j]

        elif A[j] == x:
            t += 1
            A[t], A[j] = A[j], A[t]

        else:
            # A[j] > x
            pass

    A[t+1], A[r] = A[r], A[t+1]

    return i+1, t+1



def qs_all_eq_elements(A, p, r):

    if p < r:
        q, t = partition_all_eq(A, p, r)
        qs_all_eq_elements(A, p, q-1)
        qs_all_eq_elements(A, t+1, r)

if __name__ == '__main__':

    A = [5, 1, 4, -2, 9, -5]
    print('Inp:', A)

    quicksort(A, p=0, r=len(A)-1)
    print('Basic:', A)

    A = [5, 1, 4, -2, 9, -5]
    randomized_quicksort(A, 0, len(A)-1)
    print('Randomized Partition:', A)

    A = [5, 1, 4, -2, 9, -5, -4, 3, 8, -7, 12, -25, 3, 5]
    print('\nInp:', A)
    quick_ins_sort(A, 0, len(A)-1, 6)
    print('Quick before Ins:', A)
    insertion_sort_inplace(A)
    print('Insertion sort:', A)

    A = [5, 1, 4, 5, 9, -5, -4, 3, 5, 5, 12, -25, 3, 5]
    print('\nInp:', A)
    qs_all_eq_elements(A, 0, len(A)-1)
    print('All Equals:', A)

    A = [5, 5, 5, 5, 5, 5]
    print('\nInp:', A)
    qs_all_eq_elements(A, 0, len(A) - 1)
    print('All Equals:', A)
