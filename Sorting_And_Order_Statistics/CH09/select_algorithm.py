
from Sorting_And_Order_Statistics.CH07.quick_sort import randomized_partition
import math

def find_min_max(A):
    '''
    We can find min and max of A in less than 2n time using only 3n/2 comparisons

    Procedure:
    -> Create pairs and compare numbers in pairs
    -> compare smaller of two with minimum
    -> compare larger of two with maximum

    Complexity: O(n)
    '''

    n = len(A)

    if n % 2 != 0:
        st = 1
        end = n
        minimum, maximum = A[0]
    else:
        st = 0
        end = n
        maximum = -math.inf
        minimum = math.inf

    for i in range(st, end, 2):

        minimum = min( min(A[i-1], A[i]), minimum)
        maximum = max( max(A[i-1], A[i]), maximum)

    return minimum, maximum


def selection(A, p, r, i):
    '''
    Find the ith smallest integer in A. It follows a partition approach similar to Quicksort

    Procedure:
    -> Partition array around the pivot element(x) : < x | = x | > x
    -> if i in within index p to q, recurse on left subarray
    -> if i in within index q to r, recurse on right subarray

    Features: selects without sorting
    Complexity: O(n)
    '''

    if p == r:
        return A[p]
    else:
        q = randomized_partition(A, p, r)

        k = q-p+1       # k is no. of elements on left subarray including the pivot A[q]

        if i == k:
            return A[q]
        elif i < k:
            return selection(A, p, q-1, i)
        else:
            return selection(A, q+1, r, i-k)

if __name__ == '__main__':

    A = [4, 5, 2, 1, 6, -4, -9, 23, 76, 22]
    minimum, maximum =  find_min_max(A)
    print('Min:', minimum, 'Max:', maximum)

    A = [4, 5, 2, 0, 1, 6, -4, -9, 23, 76, 22]
    i = 3
    ele = selection(A, p=0, r=len(A)-1, i=i)
    print('Select {}: {}'.format(i, ele))
