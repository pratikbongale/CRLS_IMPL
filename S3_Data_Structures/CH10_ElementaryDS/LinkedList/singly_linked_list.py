from S3_Data_Structures.CH10_ElementaryDS.LinkedList.linked_lists import *

class SLLNode(Node):

    def __init__(self, x):
        super().__init__(x)

class SinglyLinkedList(LinkedList):

    def __init__(self):
        self.head = None

    def insert(self, x):
        '''
        inserts x in the front of array
        '''

        if self.head:
            x.next = self.head

        self.head = x

    def remove_ele(self, x):
        '''
        remove element pointed to by x
        '''

        if self.head is None:
            raise EmptyLinkedListError

        if x.next is None:

            # find the node(z) before x
            # this loop can be avoided if we use sentinal node
            z = self.head
            while z.next != x:
                z = z.next

            if z.next != x:
                raise NodeNotFoundError
        else:
            z = x

        # copy the next element into current element
        z.data = z.next.data
        z.next = z.next.next

    def print_list(self):

        s = ''
        x = self.head
        while x:
            s += str(x.data) + ('->' if x.next else '')
            x = x.next

        print(s)

    def reverse(self):

        x = self.head
        y = None

        while x:
            temp = x.next
            x.next = y
            y = x
            x = temp

        self.head = y

if __name__ == '__main__':

    sll = SinglyLinkedList()

    x = Node(10)

    # test if it catches the exception
    try:
        sll.remove_ele(x)
    except EmptyLinkedListError as err:
        print(err.msg)

    # test insert functionality
    sll.insert(Node(100))
    sll.insert(Node(200))
    sll.insert(Node(300))
    sll.insert(Node(400))

    sll.print_list()
    sll.reverse()
    sll.print_list()
