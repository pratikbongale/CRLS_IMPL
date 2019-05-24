def insertion_sort_inplace(nums):

    n = len(nums)
    for j in range(1, n):
        key = nums[j]

        i = j-1

        while i >= 0 and nums[i] > key:
            nums[i+1] = nums[i]
            i = i - 1

        nums[i+1] = key

    return nums

# @sort_type('inplace')
def insertion_sort_recursive(nums, n, key):

    if n < 2:   # check length of array, if only one element, return
        return

    insertion_sort_recursive(nums, n-1, nums[n-2])

    last = n-2

    while n > 1 and nums[last] > key:
        nums[last+1] = nums[last]
        n -= 1
        last -= 1

    nums[last+1] = key

if __name__ == '__main__':

    # simple test
    arr = [5, 1, 4, -2, 9, -5]

    res = insertion_sort_inplace(arr)
    print('Inplace: ', arr == res)
    print(res)

    arr = [5, 1, 4, -2, 9, -5]
    insertion_sort_recursive(arr, len(arr), arr[-1])
    print(arr)

    # other tests are in Tests/test_sorts





