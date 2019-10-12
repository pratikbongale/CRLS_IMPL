from s3_data_structures.ch10_elementary_ds.linked_list_ds.linked_list import *
from s3_data_structures.ch10_elementary_ds.linked_list_ds.errors import *
from utilities.node_factory import *
from typing import Optional

'''
Properties:
    Doubly - double ended 
    Circular ll

Applications:
    When you want to repeatedly go around the list.
    example: multiple apps are running on a PC, give a slice of time to each app
    Eliminate the boundary conditions
    
Operations:
    Insert at the head
    Remove specified element
    Print
'''


class DoublyLinkedListCirc(LinkedList):
    # tail.next =  head and head.prev = tail

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

        self.head.prev = self.tail
        self.tail.next = self.head

    def append(self, x: DLLNode):
        '''
        Insert x at the end of list
        '''

        if self.is_empty():
            self.head = self.tail = x
        else:
            x.prev = self.tail
            self.tail.next = x
            self.tail = x

        self.head.prev = self.tail
        self.tail.next = self.head

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
            # not possible in a circular ll
            raise NodeNotFound

        if x.next is x:
            if x is self.head:
                # this is the only element in list
                self.head = self.tail = None
                return
            else:
                raise NodeNotFound

        if x is self.head:
            self.head = x.next

        elif x is self.tail:
            self.tail = x.prev

        x.next.prev = x.prev
        x.prev.next = x.next

    def print_list(self):

        s = ''
        x = self.head
        while x is not self.tail:
            s += str(x.data) + ' <-> '
            x = x.next

        s += str(x.data)

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

        self.head.prev = self.tail
        self.tail.next = self.head


if __name__ == '__main__':

    dll = DoublyLinkedListCirc()

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
