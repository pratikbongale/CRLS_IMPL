from utilities.helper_functions import print_matrix

# problem statement:
# we need to translate a text from English to French
# you need more frequent words closer to the root
# and less frequent words farther away.

inf = 10**10

def optimal_bst(p, q, n):
    '''
    find the optimal bst with best expected cost to search.

    Given:
    :param p: probability of occurence of keys in a search
    :param q: probability that a searched key does not exist
    :param n: number of keys
    :return: e(estimated cost), root(chosen roots)
    '''

    # e[1..n+1, 0..n]
    # w[1..n+1, 0..n]
    # root[1..n, 1..n]

    e = [[0 for _ in range(n+1)] for _ in range(n+2)]
    w = [[0 for _ in range(n+1)] for _ in range(n+2)]
    root = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]

    for l in range(1, n+1):
        for i in range(1, (n+1)-l+1):   # i = 1..n+1
            j = i+l-1

            e[i][j] = inf
            w[i][j] = w[i][j-1] + p[j] + q[j]

            for r in range(i, j+1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]

                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return e, root

if __name__ == '__main__':

    p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

    e, r = optimal_bst(p, q, 5)
    print_matrix(e)
    print_matrix(r)
