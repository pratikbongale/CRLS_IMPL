# select the smallest element place it at position 1, then find second smallest from the rest.
def selection_sort_inplace(nums):


    # for j in arr[1..n]:
    # - key = a[j]
    # - for i in arr[j..n]
    # -- if smallest > key:
    # --- continue

    n = len(nums)
    for j in range(n-1):
        smallest_idx = j

        for i in range(j, n):
            if nums[i] < nums[smallest_idx]:
                smallest_idx = i

        nums[smallest_idx], nums[j] = nums[j], nums[smallest_idx]

    return nums

if __name__ == '__main__':

    # simple test
    arr = [5,1,4,-2,9,-5]

    res = selection_sort_inplace(arr)
    print('Inplace: ', arr == res)
    print(res)

    # other tests are in Tests/test_sorts