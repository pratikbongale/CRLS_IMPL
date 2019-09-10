from utilities.node_factory import *

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, x):
        #  x: TreeNode

        z = self.root
        while z:
            if x.data == z.data:
                return z
            elif x.data < z.data:
                z = z.left
            else:
                z = z.right

        print('Not found')
        return None

    def insert(self, x):

        if self.root is None:
            self.root = x
        else:
            z = None
            y = self.root
            while y:
                z = y
                if x.data <= y.data:
                    y = y.left
                else:
                    y = y.right

            if x.data <= z.data:
                z.left = x
            else:
                z.right = x

            x.parent = z

    def delete(self, x):
        # here x is a pointer to element x which is to be deleted
        # if x has no children, delete it
        # if it has one child, move that child up
        # if it has two children, move x's successor up
        if x.left is None:
            self.translate(x, x.right)
        elif x.right is None:
            self.translate(x, x.left)
        else:
            y = self.minimum(x.right)
            if y != x.right:
                self.translate(y, y.right)
                y.right = x.right
                y.right.parent = y
            self.translate(x, y)
            y.left = x.left
            y.left.parent = y

    def translate(self, u, v):
        # this helper function moves the subtree
        # rooted at v to u

        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def minimum(self, root):
        x = root
        if x:
            while x.left:       # keep going to left
                x = x.left
            return x
        else:
            return None

    def maximum(self, root):
        x = root
        if x:
            while x.right:  # keep going to right
                x = x.right
            return x
        else:
            return None

    def successor(self, x):
        # if right is not None
        # leftmost node/minimum in right subtree
        # else
        # go up until you find a node which is left child of its parent, return the parent
        if x.right:
            return self.minimum(x.right)

        while x.parent:
            if x == x.parent.left:
                return x.parent

            x = x.parent

        return None

    def predecessor(self, x):
        # same logic as successor

        if x.left:
            return self.maximum(x.left)

        while x.parent:
            if x == x.parent.right:
                return x.parent

            x = x.parent

        return None

    def create_tree(self, arr):
        for i in arr:
            x = TreeNode(i)
            self.insert(x)

        return self.root

    def inorder_rec(self, x):
        if x:
            self.inorder_rec(x.left)
            print(x, end=' ')
            self.inorder_rec(x.right)


    def inorder_nonrec(self, x):
        if not self.root:
            return None

        s = []
        y = self.root

        while True:

            if y is None:
                y = s.pop()
                popped = True
                # notifies that we are ready to process a previously pushed(saved) state
                # If we dont maintain this flag, we might have an infinite loop when we reach the leaf node
                # We go left to the leaf node, pop the parent and then again go to left.
            else:
                popped = False

            if y.left and not popped:
                s.append(y)
                y = y.left
            else:
                print(y, end=' ')
                y = y.right

            if not s and not y:
                break

    def inorder_nonrec_nostack(self,  root):
        curr = root

        while curr:
            if curr.left is None:
                print(curr.data, end=' ')
                curr = curr.right
            else:
                # find the inorder predecessor
                pred = curr.left
                while pred.right is not None and pred.right != curr:
                    pred = pred.right

                if pred.right == curr:
                    pred.right = None   # reset the link
                    print(curr, end=' ')
                    curr = curr.right
                else:
                    pred.right = curr   # set the link
                    curr = curr.left

if __name__ == '__main__':

    arr = [10,24,31,29,35,40,10,8]
    bst = BinarySearchTree()
    bst.create_tree(arr)
    print('Inorder traversal recursive')
    bst.inorder_rec(bst.root)

    print('\nInorder traversal using stack')
    bst.inorder_nonrec(bst.root)

    print('\nInorder traversal using just pointers')
    bst.inorder_nonrec_nostack(bst.root)

    i = 31
    print('\nSearch', i)
    d = bst.search(TreeNode(i))
    print('Found:', d)

    print('Delete', i)
    bst.delete(d)           # TODO: Not working
    print('Inorder traversal recursive')
    bst.inorder_rec(bst.root)





