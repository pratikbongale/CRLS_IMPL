from s3_data_structures.ch10_elementary_ds.linked_list_ds.linked_list import *
from s3_data_structures.ch10_elementary_ds.linked_list_ds.errors import *
from utilities.node_factory import *
from typing import Optional

'''
Properties:
    Doubly - double ended (With tail pointer)
    Not circular
    
Applications:
    You can traverse lists forward and backward.
    You can insert anywhere in a list easily. 
    You can delete nodes very easily. 

Operations:
    Insert at the head
    Remove specified element
    Print
'''


class DoublyLinkedList(LinkedList):

    def __init__(self):
        self.head: Optional[DLLNode] = None     # if an explicit value of None is allowed, Optional is appropriate
        self.tail: Optional[DLLNode] = None

    def insert(self, x: DLLNode):
        '''
        Inserts x in the front of list
        '''

        if self.is_empty():
            self.head = self.tail = x
        else:
            x.next = self.head
            self.head.prev = x
            self.head = x

    def append(self, x: DLLNode):
        '''
        Insert x at the end of list
        '''

        if self.is_empty():
            self.head = self.tail = x
        else:
            self.tail.next = x
            x.prev = self.tail
            self.tail = self.tail.next

    def remove_ele(self, x: DLLNode):
        '''
        remove element pointed to by x
        :raises NodeNotFound
        '''

        if self.is_empty():
            raise EmptyLinkedList

        if x.next is not None:
            # x has next element
            x.next.prev = x.prev

            if x.prev is not None:
                # x has previous element
                x.prev.next = x.next

        else:
            # x.next is None
            if x.prev is not None:
                x.prev.next = None
            else:
                # x.prev is None
                if x is self.head:
                    self.head = None
                    self.tail = None
                else:
                    # here we did not search the current linked list,
                    # but this should work in all cases
                    raise NodeNotFound

    def print_list(self):

        s = ''
        x = self.head
        while x:
            s += str(x.data) + (' <-> ' if x.next else '')
            x = x.next

        print(s)

    def is_empty(self):
        return self.head is None and self.tail is None

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

    def __str__(self):
        s = ''
        x = self.head
        while x:
            s += str(x.data) + (' <-> ' if x.next else '')
            x = x.next

        return s


if __name__ == '__main__':

    dll = DoublyLinkedList()

    x = DLLNode(10)

    # test if it catches the exception
    try:
        dll.remove_ele(x)
    except EmptyLinkedList as err:
        print(err.message)

    # test insert functionality
    dll.insert(DLLNode(100))
    dll.insert(DLLNode(200))
    dll.insert(DLLNode(300))
    dll.insert(DLLNode(400))

    dll.append(DLLNode(200))
    dll.append(DLLNode(300))
    dll.append(DLLNode(400))

    dll.print_list()
