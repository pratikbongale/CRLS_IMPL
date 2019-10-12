from s3_data_structures.ch10_elementary_ds.linked_list_ds.linked_list import *
from s3_data_structures.ch10_elementary_ds.linked_list_ds.errors import *
from utilities.node_factory import *

'''
Properties:
    single linked, without tail pointer
    
Operations:
    Insert at the head          - O(1)
    Remove specified element    - O(n)
    Reverse                     - O(n)
    Search                      - O(n)
    Print                       - O(n)                       
'''

class SinglyLinkedList(LinkedList):

    def __init__(self):
        self.head = None

    def insert(self, x):
        '''
        inserts x in the front of linked list
        '''

        if not isinstance(x, SLLNode):
            x = SLLNode(x)

        if self.head:
            x.next = self.head

        self.head = x

    def remove_ele(self, x):
        '''
        remove element pointed to by x
        :raises EmptyLinkedList, NodeNotFound
        '''

        if self.head is None:
            raise EmptyLinkedList

        if x.next is None:

            # check if this is the only node
            if x is self.head:
                self.head = None    # deleting last node
                return

            # find the node 'z' before x
            z = self.head
            while z.next != x:
                z = z.next

            if z.next != x:
                raise NodeNotFound
        else:
            z = x

        # copy the next element into current element
        z.data = z.next.data
        z.next = z.next.next

    def print_list(self):
        s = ''
        x = self.head
        while x:
            s += str(x.data) + (' => ' if x.next else '')
            x = x.next

        print(s)

    def __str__(self):
        s = ''
        x = self.head
        while x:
            s += str(x.data) + (' => ' if x.next else '')
            x = x.next

        return s

    def reverse(self):

        x = self.head
        y = None

        while x:
            temp = x.next
            x.next = y
            y = x
            x = temp

        self.head = y

    def search(self, key):

        if not self.is_empty():
            x = self.head
            while x:
                if x.data == key:   # compares objects based on comparator __eq__()
                    break
                x = x.next

            if x:
                return x
            else:
                return None
        else:
            return None

    def is_empty(self):
        return self.head is None

    def merge(self, ll):
        # merge this and ll (append ll to self's tail)

        if not isinstance(ll, self.__class__):
            print('Cannot merge: Input is not an instance of SinglyLinkedList')
            return

        if self.is_empty():
            self.head = ll.head
            return

        # find the tail node
        tail = self.head
        while tail.next:
            tail = tail.next

        # append to tail
        tail.next = ll

        # update the tail
        while tail.next:
            tail = tail.next

if __name__ == '__main__':

    sll = SinglyLinkedList()

    x = SLLNode(10)

    # test if it catches the exception
    try:
        sll.remove_ele(x)
    except EmptyLinkedList as err:
        print(err.message)

    # test insert functionality
    sll.insert(SLLNode(100))
    sll.insert(SLLNode(200))
    sll.insert(SLLNode(300))
    sll.insert(SLLNode(400))

    sll.print_list()
    sll.reverse()
    sll.print_list()

    print(sll.search(200))