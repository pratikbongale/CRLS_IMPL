head = None

def insert(LL, x):
    '''
    insert x in front of LL
    '''

    global head

    if head:
        x.next = head

    head = x

def remove(LL, x):
    '''
    :param x: points to the element in LL to be removed
    '''

    global head

    if not head:
        return 'Linked List is empty'
    else:
        res = x.data
        curr = head
        while curr and curr.next != x:
            curr = curr.next

        curr.next = curr.next.next

        return res


def print_list(LL):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

if __name__ == '__main__':
    pass