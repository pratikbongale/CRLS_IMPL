
from s2_sorting_and_order_statistics.ch07_quick_sort.quick_sort import randomized_partition
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


def randomized_selection(A, p, r, i):
    '''
    Find the ith smallest integer in A, also known as ith order statistic.
    It follows a partition approach similar to Quicksort

    Procedure:
    -> Partition array around the pivot element(x) : < x | = x | > x
    -> if i in within index p to q, recurse on left subarray
    -> if i in within index q to r, recurse on right subarray

    Features: selects without sorting
    Complexity: O(n) expected, O(n^2) worst case
    '''

    if p == r:
        return A[p]
    else:
        q = randomized_partition(A, p, r)

        k = q-p+1       # k is no. of elements on left subarray including the pivot A[q]

        if i == k:
            return A[q]
        elif i < k:
            return randomized_selection(A, p, q-1, i)
        else:
            return randomized_selection(A, q+1, r, i-k)


def median_of_medians(A, i):
    '''
    Find the ith order statistic in linear time (worst case)
    '''

    # divide the array in to groups of 5
    # insertion sort each subarray/group
    # find medians from each group
    # find median-of-medians of these groups of 5
    # make that your pivot element and perform selection

    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sub)[len(sub)//2] for sub in sublists]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        pivot = median_of_medians(medians, len(medians)//2)

    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)    # pivot element's index

    if i == k:
        return pivot
    elif i < k:
        return median_of_medians(low, i)
    else:
        return median_of_medians(high, i-k-1)



if __name__ == '__main__':

    A = [4, 5, 2, 1, 6, -4, -9, 23, 76, 22]
    minimum, maximum =  find_min_max(A)
    print('Min:', minimum, 'Max:', maximum)

    A = [4, 5, 2, 0, 1, 6, -4, -9, 23, 76, 22]
    i = 1
    ele = randomized_selection(A, p=0, r=len(A)-1, i=i)
    print('Select {}: {}'.format(i, ele))

    A = [4, 5, 2, 0, 1, 6, -4, -9, 23, 76, 22]
    i = 1
    ele = median_of_medians(A, i-1)
    print('Median of Medians {}: {}'.format(i, ele))