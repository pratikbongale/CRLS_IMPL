import math
from utilities.helper_functions import print_matrix

# Recurrence:
# m[i,j]  = min:i<=k<=j ( m[i,k] + m[k+1,j] + p[i-1]*p[k]*p[j] )

def min_ops_mat_mult(arr):
    # arr: a list containing dimensions of each matrix
    #      in the form of a tuple eg. [(10,100), (100,50), (50,25)]

    n = len(arr)
    m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for l in range(1, n):   # length of matrices considered

        for i in range(0, n-l):
            j = i+l

            m[i][j] = math.inf      # m[0,1], m[1,2], m[2,3] ...

            for k in range(i, j):
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + arr[i][0]*arr[k][1]*arr[j][1])

    print_matrix(m)

    return m[0][n-1]

def min_ops_mat_mul_solution(arr):
    raise NotImplementedError


if __name__ == '__main__':

    arr = [(30,35), (35,15), (15,5), (5,10), (10,20), (20,25)]
    print(min_ops_mat_mult(arr))    # 15125
