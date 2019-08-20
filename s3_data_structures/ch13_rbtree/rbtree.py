from s3_data_structures.ch12_bst.bst import TreeNode
from s3_data_structures.ch12_bst.bst import BinarySearchTree

RED = 'r'
BLACK = 'b'

class RBTreeNode(TreeNode):
    def __init__(self, data, color=RED):
        super(RBTreeNode, self).__init__(data)
        self.color = color  # new node must be red by default

    def __str__(self):
        return str(self.data) + ':' + self.color

    def __eq__(self, other):
        if isinstance(other, RBTreeNode):
            return self.data == other.data and self.color == other.color

    def __ne__(self, other):
        if isinstance(other, RBTreeNode):
            return self.data != other.data or self.color != other.color

class RBTree(BinarySearchTree):
    # properties:
    # 1. Every node is either black or red
    # 2. Root must be black
    # 3. Leaf must be black
    # 4. a red node must have both black children
    # 5. Maintain black height(# black nodes on path to leaf) from any given node

    def __init__(self):
        super(RBTree, self).__init__()
        self.nil = RBTreeNode(None)     # sentinel node
        self.nil.color = BLACK
        self.root = self.nil

    def insert(self, z):

        x = self.root
        y = self.nil     # we maintain NIL instead of None
        while x != self.nil:
            y = x
            if z.data <= x.data:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.data <= y.data:
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.color = RED       # helps easy fixes
        self.rbt_fixup(z)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.nil:
            x.right.parent = y

        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = y

        x.right = y
        y.parent = x

    def rbt_fixup(self, z):
        # z.p.p exists always because:
        # - we know that root is always black
        # - while loop condition checks if the parent is red

        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                u = z.parent.parent.right
                if u.color == RED:
                    # case 1
                    # flip colors
                    u.color = BLACK
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    # uncle node is black

                    # case2
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    # case 3
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else:
                u = z.parent.parent.left
                if u.color == RED:
                    # case 1
                    # flip colors
                    u.color = BLACK
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    # case 2
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    # csae 3
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)

        self.root.color = BLACK


    def create_tree(self, a):
        for ele in a:
            node = RBTreeNode(ele)  # red node
            self.insert(node)

    def search(self, z):
        x = self.root
        while x != self.nil:
            if x == z:
                break
            elif z.data < x.data:
                x = x.left
            else:
                x = x.right

        return x

    def print_tree(self):

        q = [self.root]
        while q:
            z = []
            print([str(t) for t in q])
            for x in q:
                if x != self.nil:
                    z.append(x.left)
                    z.append(x.right)

            q = z

if __name__ == '__main__':
    # create a sentinel node
    # root and all leaves point to this sentinel node

    arr = [10,24,8]
    arr1 = [10,24,31,29,35,40,10,8]
    rbt = RBTree()
    # rbt.create_tree(arr)
    rbt.create_tree(arr1)

    # tetsing insert method
    rbt.print_tree()

    # testing search
    print('\n\nSearch Node')
    t = rbt.search(RBTreeNode(10, BLACK))
    print('Node found:', t)

    # testing right rotate
    print('Right rotate')
    if t != rbt.nil:
        rbt.right_rotate(t)

    rbt.print_tree()

    t = rbt.search(RBTreeNode(8, RED))
    print('Inorder traversal recursive')
    rbt.inorder_rec(rbt.root)

    # testing left rotate by reversing the previous right rotate
    print('\n\nLeft rotate')
    if t != rbt.nil:
        rbt.left_rotate(t)

    rbt.print_tree()




