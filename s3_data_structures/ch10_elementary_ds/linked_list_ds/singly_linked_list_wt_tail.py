from s3_data_structures.ch10_elementary_ds.linked_list_ds.linked_list import *
from s3_data_structures.ch10_elementary_ds.linked_list_ds.errors import *
from utilities.node_factory import *

'''
Properties:
    single linked with tail pointer
    
Applications:
    Use only when:
        You only need to insert at the front or back of the list
        You only need to delete from the front of the list
        You only need to traverse the list in the forward direction 
        
Operations:
    Insert at the head
    Append to the tail
    Remove specified element
    reverse
    search
    Print
'''

class SinglyLinkedList(LinkedList):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, x):
        '''
        inserts x in the front of linked list
        '''

        if not isinstance(x, SLLNode):
            x = SLLNode(x)

        if self.head:
            x.next = self.head
        else:
            self.head = x
            self.tail = x
            
    def append(self, x: SLLNode):
        '''
        appends x to the end of linked list
        :param x:
        :return:
        '''

        if not isinstance(x, SLLNode):
            x = SLLNode(x)

        if not self.is_empty():
            self.tail.next = x
            self.tail = self.tail.next
        else:
            self.head = self.tail = x

    def remove_ele(self, x):
        '''
        remove element pointed to by x
        '''

        if self.head is None:
            raise EmptyLinkedList

        if x.next is None:

            # find the node(z) before x
            # this loop can be avoided if we use sentinal node
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

        self.tail = self.head
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

        if not isinstance(ll, self.__class__):
            print('Cannot merge: Input is not an instance of SinglyLinkedList')

        if self.tail:
            self.tail.next = ll.head
            self.tail = ll.tail
        else:
            self.head = self.tail = ll.head


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