from s3_data_structures.ch10_elementary_ds.stack_ds.my_stack import MyStack
from s3_data_structures.ch10_elementary_ds.stack_ds.errors import StackEmptyError, StackOverflowError
from typing import Any


class ListStack(MyStack):

    # fixed size stack implemented with python lists
    def __init__(self, size=5):
        super().__init__()
        self.stack_size: int = size
        self.top: int = -1
        self.stack = [None]*self.stack_size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.stack_size-1

    def push(self, x: Any):
        if self.is_full():
            raise StackOverflowError

        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.is_empty():
            raise StackEmptyError

        popped_ele = self.stack[self.top]
        self.top -= 1

        return popped_ele

    def __str__(self):
        s = ''
        s += ' '.join([str(x) for x in self.stack])
        return s

class DynamicListStack(ListStack):

    def __init__(self, initial_size: int = 10):
        super().__init__(initial_size)
        self.threshold: float = 0.9
        self.stack_length: int = 0       # stores the number of elements currently in stack

    def push(self, x: Any):
        if self.stack_length >= self.stack_size * self.threshold:
            self.stack.extend([None]*len(self.stack))   # double the current stack size
            self.stack_size = len(self.stack)

        try:
            super().push(x)
            self.stack_length += 1
        except StackOverflowError as e:
            print(e.message)


if __name__ == '__main__':

    print('Testing static list stack with 10 elements')
    ls = ListStack(10)

    print('PUSH')
    for i in range(100):
        try:
            ls.push(i+1)
            # print(str(i+1))
        except StackOverflowError as e:
            print(e.message)
            break

    print('Current stack:', ls.stack)

    print('POP')
    for i in range(100):
        try:
            x = ls.pop()
            # print(x)
        except StackEmptyError as e:
            print(e.message)
            break

    print('Current stack:', ls.stack)

    print('\n\nTesting dynamic list stack')
    dyn_ls = DynamicListStack(10)

    print('PUSH')
    for i in range(50):
        try:
            dyn_ls.push(i + 1)
            # print(str(i + 1))
        except StackOverflowError as e:
            print(e.message)
            break

    print('Current stack:', dyn_ls.stack)

    print('POP')
    for i in range(50):
        try:
            x = dyn_ls.pop()
            # print(x)
        except StackEmptyError as e:
            print(e.message)
            break

    print('Current stack:', dyn_ls.stack)