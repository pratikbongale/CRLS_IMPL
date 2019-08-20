from s3_data_structures.ch13_rbtree.rbtree import RBTree, RBTreeNode, BLACK, RED

class OrderStatisticTreeNode(RBTreeNode):

    def __init__(self, data, color=RED):
        super().__init__(data, color)
        self.size = 0

    # eq and ne methods are implemented in RBTree, we can just use that

    def __str__(self):
        return str(self.data) + ':' + self.color + ':' + str(self.size)

class OrderStatisticTree(RBTree):

    def __init__(self):
        super().__init__()
        self.nil = OrderStatisticTreeNode(None)
        self.nil.color = BLACK
        self.nil.size = 0

    def insert(self, z):
        super().insert(z)
        x = z
        while x != self.nil:
            x.size += 1
            x = x.parent

    def get_size(self, node):
        s = 0
        if node != self.nil:
            s = node.left.size + node.right.size + 1
        return s

    def os_select(self, x, i):
        # return: ith order statistic in subtree rooted at x
        # ith smallest number in subtree rooted at x
        r = x.size - x.right.size
        if i == r:
            return x
        elif i < r:
            return self.os_select(x.left, i)
        else:
            return self.os_select(x.right, i-r)

    def os_rank(self, x):
        # return: rank of element x

        # if its a left child, recursive call: rank(predecessor(x)) + 1
        # if right child, go up to the root adding all sizes
        r = x.left.size + 1
        while x != self.nil:
            if x != self.root and x == x.parent.right:
                r += x.parent.left.size + 1
            else:
                break

            x = x.parent

        return r

    def left_rotate(self, x):
        super().left_rotate(x)
        y = x.parent
        y.size = x.size
        x.size = self.get_size(x)

    def right_rotate(self, y):
        super().right_rotate(y)
        x = y.parent
        x.size = y.size
        y.size = self.get_size(y)

    def create_tree(self, a):
        for ele in a:
            node = OrderStatisticTreeNode(ele)
            self.insert(node)

if __name__ == '__main__':

    ost = OrderStatisticTree()

    arr = [10,24,31,29,35,40,10,8]
    ost.create_tree(arr)

    ost.print_tree()

    # print all ranks, 1..n (inorder)
    for i in range(1, len(arr)+1):
        print('Rank-', i, 'Element-', ost.os_select(ost.root, i))

    t = ost.search(OrderStatisticTreeNode(40))
    print('Rank of ', t, ' -', ost.os_rank(t))

