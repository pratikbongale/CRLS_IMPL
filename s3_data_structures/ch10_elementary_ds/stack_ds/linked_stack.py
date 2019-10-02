from s3_data_structures.ch10_elementary_ds.stack_ds.my_stack import MyStack
from s3_data_structures.ch10_elementary_ds.stack_ds.errors import StackOverflowError, StackEmptyError
from utilities.node_factory import SLLNode, DLLNode, NodeGenerator


class LinkedStack(MyStack):

    def __init__(self):
        super().__init__()
        self.top: DLLNode           # easy to remove, need a way to go to previous element
        self.length: int = 0        # number of elements stack holds currently
        self.threshold: int = 1000  # more than thousand nodes

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # never really full, but need to set a stack overflow somewhere
        # otherwise the python will eat entire memory
        return self.length == self.threshold

    def push(self, x):

        if self.is_full():
            raise StackOverflowError

        if not isinstance(x, DLLNode):
            x = DLLNode(x)  # wrap it around a SLL node object

        if self.top:
            self.top.next = x
            x.prev = self.top
            self.top = x
        else:
            self.top = x

        self.length += 1

    def pop(self):

        if self.is_empty():
            raise StackEmptyError

        removed_ele = self.top.data     # get the node data
        self.top = self.top.prev

        if self.top:
            self.top.next = None

        self.length -= 1

        return removed_ele

    def __str__(self):
        s = '<- TOP'

        t = self.top
        while t:
            s = str(t.data) + ' ' + s
            t = t.prev

        return s

if __name__ == '__main__':

    # testing simple interger queue
    ls = LinkedStack()

    arr = [ls.push(x) for x in range(10, 101, 10)]
    print('Initial stack', ls)

    print('Pop()')
    ls.pop()
    print(ls)

    # testing SLL
    n1 = NodeGenerator.get_dll_node(10)
    n2 = NodeGenerator.get_dll_node(20)

    ls = LinkedStack()
    ls.push(n1)

    print('\n\nStack with one element:', ls)

    try:
        ele = ls.pop()  # will remove the only element in theh queue
        print('Removed inserted element:', ele)

        ele = ls.pop()  # will throw an exception
    except StackEmptyError as e:
        print('Error:', e.message)

    ls.push(n2)
    ls.push(n1)
    print(ls)