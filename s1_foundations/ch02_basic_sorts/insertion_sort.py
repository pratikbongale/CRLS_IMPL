# @sort_type('inplace')
def insertion_sort_inplace(arr):

    n = len(arr)
    for j in range(1, n):
        key = arr[j]

        i = j-1

        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1

        arr[i+1] = key

    return arr

# @sort_type('inplace')
def insertion_sort_recursive(arr):
    n = len(arr)

    key = arr[-1] if n > 0 else None
    insertion_sort_recursive_helper(arr, n, key)

    return arr

# @sort_type('inplace')
def insertion_sort_recursive_helper(arr, n, key):

    if n < 2:   # check length of array, if only one element, return
        return

    insertion_sort_recursive_helper(arr, n-1, arr[n-2])

    last = n-2

    while n > 1 and arr[last] > key:
        arr[last+1] = arr[last]
        n -= 1
        last -= 1

    arr[last+1] = key

if __name__ == '__main__':

    # simple test
    arr = [5, 1, 4, -2, 9, -5]
    print('Input arr:', arr)

    res = insertion_sort_inplace(arr)
    print('Inplace:', arr == res)
    print(res)

    arr = [5, 1, 4, -2, 9, -5]
    insertion_sort_recursive(arr)
    print(arr)

    # other tests are in Tests/test_sorts





