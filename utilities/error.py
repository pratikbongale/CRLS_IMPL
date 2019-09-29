# having a common base class we know that every
# custom exception class will at least have the property "message"
# which gives a description of what was the error
class Error(Exception):

    __slots__ = ['message']

    def __init__(self, msg):
        self.message = msg

