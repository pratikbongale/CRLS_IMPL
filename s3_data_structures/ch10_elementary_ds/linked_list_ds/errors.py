from utilities.error import Error


class EmptyLinkedList(Error):
    def __init__(self):
        super().__init__('Linked List is Empty')
        self.suggest = 'Please insert at least one element in the Linked List.'


class NodeNotFound(Error):
    def __init__(self):
        super().__init__('LL Node not found')
        self.suggest = 'The node is not present in linked list'