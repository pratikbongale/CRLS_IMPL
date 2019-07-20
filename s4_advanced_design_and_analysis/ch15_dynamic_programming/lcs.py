from utilities.helper_functions import print_matrix

def lcs_length(x, y):
    m = len(x)
    n = len(y)

    c = [[0] * (n+1) for _ in range(m+1)]
    b = [[''] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "\\"

            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "|"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "_"

    return c, b

def print_lcs(b, x, i, j):

    if i == 0 or j == 0:
        return

    if b[i][j] == "\\":
        print_lcs(b, x, i-1, j-1)
        print(x[i-1], end='')
    elif b[i][j] == "|":
        print_lcs(b, x, i-1, j)
    else:
        print_lcs(b, x, i, j-1)

if __name__ == '__main__':

    x = "abcbdab"
    y = "bdcaba"
    m = len(x)
    n = len(y)

    c, b = lcs_length(x, y)

    print_matrix(c)

    print_matrix(b)

    print_lcs(b, x, m, n)
