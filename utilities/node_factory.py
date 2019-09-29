class NodeGenerator:

    @staticmethod
    def get_sll_node(x):    # static methods are used as utility functions
        return SLLNode(x)

    @staticmethod
    def get_dll_node(x):    # static methods cannot access/modify class state
        return DLLNode(x)

    @staticmethod
    def get_binary_tree_node(x):    # static methods take inp some args and work on them and return something
        return BinaryTreeNode(x)

    @staticmethod
    def get_graph_node(x):
        return GraphNode(x)


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


class TreeNode(Node):
    def __init__(self, x):
        super().__init__(x)
        self.children = list()
        self.parent = None

    def add_child(self, x):
        self.children.append(x)

    def __str__(self):

        s = str(self.data) + ' => '
        s += ' '.join([str(x) for x in self.children])

        return s

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.data == other.data

    def __ne__(self, other):
        if isinstance(other, TreeNode):
            return self.data != other.data


class BinaryTreeNode(TreeNode):
    def __init__(self, x, left=None, right=None):
        super().__init__(x)
        self.left = left
        self.right = right

        if left:
            self.add_child(left)

        if right:
            self.add_child(right)


class GraphNode(Node):
    """
     only valid for adjacency tree
    """

    __slots__ = ["data", "color", "dist", "parent"]

    def __init__(self, x=None):
        super().__init__(x)

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if isinstance(GraphNode, other):
            return self.data == other.data