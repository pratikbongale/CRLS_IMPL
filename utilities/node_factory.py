
class NodeGenerator():

    def get_sll_node(self, val):
        return SLLNode(val)

    def get_dll_node(self, val):
        return DLLNode(val)

    def get_binary_tree_node(self, val):
        pass

class Node:
    def __init__(self, x):
        self.data = x

    def __str__(self):
        return str(self.data)

class SLLNode(Node):

    def __init__(self, x):
        super().__init__(x)
        self.next = None

class DLLNode(Node):

    def __init__(self, x):
        super().__init__(x)
        self.prev = None
        self.next = None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.data == other.data

    def __ne__(self, other):
        if isinstance(other, TreeNode):
            return self.data != other.data