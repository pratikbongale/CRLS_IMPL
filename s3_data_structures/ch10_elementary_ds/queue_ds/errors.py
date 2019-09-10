from utilities.error import Error


class EmptyQueueError(Error):
    def __init__(self):
        super().__init__('Queue is Empty')
        self.suggest = 'Please insert at least one element in the queue.'

class FullQueueError(Error):
    def __init__(self):
        super().__init__('Queue is full')
        self.suggest = 'Please delete at least one element from the queue to put this element'