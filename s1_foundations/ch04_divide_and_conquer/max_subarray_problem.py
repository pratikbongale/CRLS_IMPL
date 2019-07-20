import math
from itertools import accumulate

def max_subarray_brute(A):
    n = len(A)

    if n < 1:
        return A

    max_sum = -math.inf
    low = high = -1

    acc = list(accumulate(A))

    for i in range(n):
        for j in range(i, n):
            if i == j:
                s = A[i]
            else:
                s = (acc[j] - acc[i-1]) if i > 0 else acc[j]

            if s > max_sum:
                max_sum = s
                low = i
                high = j

    return (low, high, max_sum)

def max_crossing_subarray_crls(A, low, mid, high):

    left_max = -1
    left_sum = -math.inf
    curr_sum = 0
    for i in range(mid, low-1, -1):
        curr_sum += A[i]
        if curr_sum > left_sum:
            left_sum = curr_sum
            left_max = i

    right_max = -1
    right_sum = -math.inf
    curr_sum = 0
    for i in range(mid+1, high+1):
        curr_sum += A[i]
        if curr_sum > right_sum:
            right_sum = curr_sum
            right_max = i

    return (left_max, right_max, left_sum+right_sum)

def max_subarray_crls(A, low, high):
    '''
    O(nlogn) - using divide and conquer approach
    :param A: inp array
    :param low:
    :param high:
    :return: (low_idx, high_idx, sum)
    '''

    if low == high:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray_crls(A, low, mid)
        right_low, right_high, right_sum = max_subarray_crls(A, mid+1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray_crls(A, low, mid, high)

        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def max_subarray_linear(A):
    pass

if __name__ == '__main__':

    A = [10, 11, 7, 10, 6]
    A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

    A = [A[i] - A[i - 1] for i in range(1, len(A))]

    l, h, s = max_subarray_brute(A)
    print('Buy:', l, 'Sell:', h + 1, 'Profit:', s)

    l, h, s = max_subarray_crls(A, 0, len(A)-1)
    print('Buy:', l, 'Sell:', h + 1, 'Profit:', s)