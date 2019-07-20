def print_matrix(mat):
    # assuming mat has atleast 1 row x 1 col


    r = len(mat)
    c = len(mat[0])

    print('\n')

    for i in range(r):
        for j in range(c):
            print('{:{width}}'.format(mat[i][j], width=15), end='')
        print('\n')