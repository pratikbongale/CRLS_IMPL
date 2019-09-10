import math
from itertools import accumulate

def max_subarray_brute(A):
    '''
    O(n^2) - using brute force, check all sub-arrays
    :param A: inp array
    :return: low_idx, high_idx, max_sum
    '''
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

    return low, high, max_sum


def max_subarray_crls(A):
    return max_subarray_crls_helper(A, low=0, high=len(A)-1)


def max_subarray_crls_helper(A, low, high):
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
        left_low, left_high, left_sum = max_subarray_crls_helper(A, low, mid)
        right_low, right_high, right_sum = max_subarray_crls_helper(A, mid+1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray_crls(A, low, mid, high)

        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


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


def max_subarray_linear_basic(A):
    '''
    O(n) - using basic Kadane's algorithm
    Gives max sum = 0 if all numbers are negative
    :param A: inp array
    :return:
    '''

    # go on collecting the curr_sum and
    # make sum = 0 if it drops below 0
    # this method fails if inp has all negative numbers

    curr_sum = 0
    max_sum = 0
    max_low = low = 0
    max_high = high = 0

    for i in range(len(A)):
        curr_sum += A[i]
        if curr_sum < 0:
            curr_sum = 0
            low = i+1
        elif curr_sum > max_sum:
            max_sum = curr_sum
            max_low = low
            max_high = high

        high += 1

    return max_low, max_high, max_sum

def max_subarray_linear(A):
    '''
    O(n) - using Kadane's algorithm, works for all inputs
    :param A: inp array
    :return:
    '''

    # go on collecting the curr_sum and
    # make sum = 0 if it drops below 0
    # this method fails if inp has all negative numbers

    if A is None or len(A) == 0:
        return (None, None, None)

    curr_sum = A[0]
    max_sum = A[0]
    max_low = low = 0
    max_high = high = 0

    for i in range(1, len(A)):

        if curr_sum + A[i] < A[i]:
            curr_sum = A[i]
            low = i
            high = i
        else:
            curr_sum = curr_sum + A[i]
            high += 1

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_low = low
            max_high = high

    return max_low, max_high, max_sum

if __name__ == '__main__':

    # A = [10, 11, 7, 10, 6]
    # A = [-10, 11, 2, 3, 8, -5, 6, -10]
    A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    # A = [15, 8, 6, 3, 0]

    A = [A[i] - A[i - 1] for i in range(1, len(A))]

    print('Inp', A)

    l, h, s = max_subarray_brute(A)
    print('Low:', l, 'High:', h, 'Max sum:', s)

    l, h, s = max_subarray_crls(A, 0, len(A)-1)
    print('Low:', l, 'High:', h, 'Max sum:', s)

    l, h, s = max_subarray_linear_basic(A)
    print('Low:', l, 'High:', h, 'Max sum:', s)

    l, h, s = max_subarray_linear(A)
    print('Low:', l, 'High:', h, 'Max sum:', s)