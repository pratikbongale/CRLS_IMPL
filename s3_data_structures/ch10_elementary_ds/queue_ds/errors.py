from utilities.myexception import MyException


class EmptyQueueError(MyException):
    def __init__(self):
        super().__init__('Queue is Empty')
        self.suggest = 'Please insert at least one element in the queue.'


class FullQueueError(MyException):
    def __init__(self):
        super().__init__('Queue is full')
        self.suggest = 'Please delete at least one element from the queue to put this element'