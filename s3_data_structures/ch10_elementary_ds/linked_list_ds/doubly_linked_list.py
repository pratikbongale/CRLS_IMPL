from s3_data_structures.ch10_elementary_ds.linked_list_ds.linked_list import *
from utilities.node_factory import *

'''
Not circular
Doubly - double ended
Insert at the head
Remove specified element
Print
'''

class DoublyLinkedList(LinkedList):

    def __init__(self):
        self.head = None

    def insert(self, x):
        '''
        inserts x in the front of array
        '''

        if self.head:
            x.next = self.head
            self.head.prev = x

        self.head = x

    def remove_ele(self, x):
        '''
        remove element pointed to by x
        '''

        if self.head is None:
            raise EmptyLinkedListError

        if x.next:
            # if x has next element
            x.next.prev = x.prev
        else:
            # x.next is None
            if x.prev:
                x.prev.next = None
            else:
                # x.prev is None
                if x == self.head:
                    self.head = None
                else:
                    raise NodeNotFoundError

    def print_list(self):

        s = ''
        x = self.head
        while x:
            s += str(x.data) + ('<->' if x.next else '')
            x = x.next

        print(s)

if __name__ == '__main__':

    dll = DoublyLinkedList()

    x = DLLNode(10)

    # test if it catches the exception
    try:
        dll.remove_ele(x)
    except EmptyLinkedListError:
        print('Linked List is Empty')

    # test insert functionality
    dll.insert(DLLNode(100))
    dll.insert(DLLNode(200))
    dll.insert(DLLNode(300))
    dll.insert(DLLNode(400))

    dll.print_list()
