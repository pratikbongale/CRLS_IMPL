def fractional_knapsack(w, v, max_wt):
    '''
    find the most value you can fit in a bag of weight m
    :param w: array of weigths of each item
    :param v: array of value of each item
    :param max_wt: max weight the knapsack can carry
    :return: knapsack and its contents
    '''

    # calculate value per pound
    vpp = list()
    for i in range(len(w)):
        vpp.append(v[i]/w[i])

    # get sorted indices (descending order)
    s_indices = [i[0] for i in sorted(enumerate(vpp), key=lambda x:-x[1])]

    curr_wt = 0
    res = []

    i = 0

    for i in s_indices:

        if w[i] + curr_wt > max_wt:
            break
        else:
            curr_wt += w[i]
            res.append((i, w[i], v[i]))

    diff_wt = max_wt - curr_wt
    if diff_wt > 0:
        res.append((i, diff_wt, vpp[i]*diff_wt))

    return res

if __name__ == '__main__':
    w = [10, 20, 30]
    v = [60, 100, 120]
    max_wt = 50

    print(fractional_knapsack(w, v, max_wt))