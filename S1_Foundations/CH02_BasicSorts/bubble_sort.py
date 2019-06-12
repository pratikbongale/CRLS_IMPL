def bubble_sort_inplace(A):

    n = len(A)
    for j in range(n-1):
        for i in range(n-1, j, -1):
            if A[i-1] > A[i]:
                # swap
                A[i-1], A[i] = A[i], A[i-1]

    res = A

    return res

if __name__ == '__main__':

    # simple test
    arr = [5, 1, 4, -2, 9, -5]

    res = bubble_sort_inplace(arr)
    print('Inplace: ', arr == res)
    print(res)