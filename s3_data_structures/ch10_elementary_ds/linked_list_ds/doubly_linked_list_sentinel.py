from s3_data_structures.ch10_elementary_ds.linked_list_ds.linked_list import *
from s3_data_structures.ch10_elementary_ds.linked_list_ds.errors import *
from utilities.node_factory import *
from typing import Optional

'''
Properties:
    Doubly - double ended 
    Contains a dummy node (sentinel node) at front of the list points to first and last elements
    Do not need to maintain head and tail pointers
    To insert in front s_node.prepend, to append to last s_node.append

Applications:
    Simplifies implementation
    Eliminate the boundary conditions, updates on head and tail
'''


class DoublyLinkedListSentinel(LinkedList):

    def __init__(self):
        # sentinel node is at the front of list
        self.sentinel: Optional[DLLNode] = DLLNode(x='Sentinel')
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def insert(self, x: DLLNode):
        '''
        Inserts x in the front of list
        '''

        if self.is_empty():

            self.sentinel.next = x
            self.sentinel.prev = x
            x.next = self.sentinel
            x.prev = self.sentinel

        else:

            x.prev = self.sentinel
            x.next = self.sentinel.next
            self.sentinel.next.prev = x
            self.sentinel.next = x

    def append(self, x: DLLNode):
        '''
        Insert x at the end of list
        '''

        if self.is_empty():

            self.sentinel.next = x
            self.sentinel.prev = x
            x.next = self.sentinel
            x.prev = self.sentinel

        else:

            x.next = self.sentinel
            x.prev = self.sentinel.prev
            self.sentinel.prev.next = x
            self.sentinel.prev = x

    def remove_ele(self, x: DLLNode):
        '''
        remove element pointed to by x
        :raises NodeNotFound, EmptyLinkedList
        '''

        if not isinstance(x, DLLNode):
            print('Incorrect type in input, expected DLLNode')
            return

        if self.is_empty():
            raise EmptyLinkedList

        if x.next is None or x.prev is None:
            raise NodeNotFound

        if x.next is self.sentinel:
            x.prev.next = self.sentinel
            self.sentinel.prev = x.prev
        elif x.prev is self.sentinel:
            x.next.prev = self.sentinel
            self.sentinel.next = x.next
        else:
            x.prev.next = x.next
            x.next.prev = x.prev

    def print_list(self):

        s = ''
        x = self.sentinel.next
        while x is not self.sentinel.prev:
            s += str(x.data) + ' <-> '
            x = x.next

        s += str(x.data)

        print(s)

    def is_empty(self):
        return self.sentinel.next is self.sentinel and self.sentinel.prev is self.sentinel

    def merge(self, dll):

        if not isinstance(dll, self.__class__):
            print('Cannot merge: dll not an instance of DoublyLinkedList')
            return

        if self.is_empty():
            self.head = dll.head
            self.tail = dll.tail
        else:
            self.tail.next = dll.head
            self.tail = dll.tail

        self.head.prev = self.tail
        self.tail.next = self.head


if __name__ == '__main__':

    dll = DoublyLinkedListSentinel()

    x = DLLNode(10)

    # test if it catches the exception
    try:
        dll.remove_ele(x)
    except EmptyLinkedList as err:
        print(err.message)
    except NodeNotFound as e:
        print(e.message)

    # test insert functionality
    dll.insert(DLLNode(100))
    dll.insert(DLLNode(200))
    dll.insert(DLLNode(300))
    dll.insert(DLLNode(400))

    dll.append(DLLNode(200))
    dll.append(DLLNode(300))
    dll.append(DLLNode(400))

    dll.print_list()
