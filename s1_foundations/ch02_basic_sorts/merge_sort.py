import math

def merge_sort_old(nums):
    # divide
    # conquer
    # merge

    n = len(nums)

    if n <= 1:
        return nums

    mid = n // 2
    left = merge_sort_old(nums[:mid])
    right = merge_sort_old(nums[mid:])
    return merge_old(left, right)

def merge_old(a, b):
    # merge two sorted lists
    i = j = 0
    c = list()
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c


def merge_sort_inplace(A):
    merge_sort_inplace_helper(A, p=0, r=len(A)-1)


def merge_sort_inplace_helper(A, p, r):
    # merge A[p..r]
    if p < r:
        q = (p+r)//2        # floor division by default
        merge_sort_inplace_helper(A, p, q)
        merge_sort_inplace_helper(A, q+1, r)
        merge_crls(A, p, q, r)


def merge_crls(A, p, q, r):
    #  assuming p <= q <= r

    n1 = q - p + 1      # no. of elements in left array
    n2 = r - q          # no. of elements in right array

    left = list()
    right = list()

    for i in range(n1):
        left.append(A[p+i])

    for i in range(n2):
        right.append(A[q+1+i])  # start copying from (q+1)th index

    left.append(math.inf)
    right.append(math.inf)

    i = j = 0
    for k in range(p,r+1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1


if __name__ == '__main__':

    # simple test
    arr = [5,1,4,-2,9,-5]

    res = merge_sort_old(arr)
    print('Inplace: ', arr == res)
    print(res)

    merge_sort_inplace(arr)
    print(arr)

    # other tests are in Tests/test_sorts