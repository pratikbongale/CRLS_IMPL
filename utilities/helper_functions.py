def print_matrix(mat):
    # assuming mat has atleast 1 row x 1 col

    r = len(mat)
    c = len(mat[0])

    print('\n')

    for i in range(r):
        for j in range(c):
            print('{:{width}}'.format(mat[i][j], width=15), end='')
        print('\n')


def print_binary_tree(root):

    q = [root]
    while q:
        z = []
        print([str(t) for t in q])
        for x in q:
            if x:
                z.append(x.left)
                z.append(x.right)

        q = z


def print_adj_graph(adj_list):
    for u in adj_list:
        print(str(u) + ' : ', end='')
        print([str(x) for x in adj_list[u]], end='')
        print()