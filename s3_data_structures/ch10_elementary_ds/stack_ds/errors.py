from utilities.myexception import MyException

class StackOverflowError(MyException):

    def __init__(self):
        super().__init__('Stack is full, cannot push more elements')
        self.suggest = 'Please pop a few elements to push more elements'


class StackEmptyError(MyException):

    def __init__(self):
        super().__init__('Stack is empty')
        self.message = 'Please push a few elements before trying to pop'