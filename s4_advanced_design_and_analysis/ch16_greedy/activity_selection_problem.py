# given a set of activities S = [a1, a2, a3, ...], find the largest number of activities
# that can share an exclusive resource.

def activity_select_rec(s, f, k, n):
    '''
    Assumes that all activities are sorted by their finish time.
    :param s: start times of activities
    :param f: finish times of activities
    :return: selected activities a1, a2 ...
    '''

    # Algo:
    # select the activity with earliest finish time
    # tail recursion with Sk(all activities that start after ak finishes)

    m = k+1  # select the first activity - Greedy choice

    while m <= n and s[m] < f[k]:
        m += 1

    if m <= n:
        return [m] + activity_select_rec(s, f, m, n)
    else:
        return []

def activity_select_iter(s, f):
    res = [1]
    k = 1
    n = len(s)-1
    for i in range(2, n+1):
        if s[i] >= f[k]:
            res.append(i)
            k = i

    return res


if __name__ == '__main__':
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    r1 = activity_select_rec(s, f, 0, len(s)-1)
    r2 = activity_select_iter(s, f)

    print('recursive:', r1)
    print('iterative:', r2)



