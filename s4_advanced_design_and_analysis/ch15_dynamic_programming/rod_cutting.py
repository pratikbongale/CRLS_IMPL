def max_rod_cut_value(p, n):
    # p: dictionary of prices for rods of length different lengths
    # n: rod size
    # return: max value that can be gained by cutting rod of size n

    r = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(1, i+1):
            r[i] = max(r[i], p[j]+r[i-j])

    return r[n]

def max_rod_cut_sol(p, n):
    # returns the solution of cuts

    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if r[i] < p[j] + r[i - j]:
                r[i] = p[j] + r[i - j]
                s[i] = j

    # construct the solution from array s[]
    i = n
    res = []
    while i > 0:
        res.append(s[i])
        i = i - s[i]

    return res

if __name__ == '__main__':
    p = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}
    n = 6
    print('Max value for {} = {}'.format(n, max_rod_cut_value(p, n)))
    print('Solution', max_rod_cut_sol(p, n))
