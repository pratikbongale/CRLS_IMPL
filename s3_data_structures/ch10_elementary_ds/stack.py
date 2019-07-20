
top = -1    # points to element at top of stack
def push(S, x):
    global top

    if is_full(S):
        return 'Stack Overflow'

    else:
        top += 1
        S[top] = x

def is_full(S):
    return top+1 == len(S)

def pop(S):
    global top

    if is_empty(S):
        return 'Stack Underflow'
    else:
        res = S[top]
        top = top - 1
        return res

def is_empty(S):
    return top == -1


if __name__ == '__main__':

    stack_size = 5
    S = [0] * stack_size

    push(S, 10)
    print(S)
    push(S, 15)
    print(pop(S))
    push(S, 22)
    print(S)
    print(pop(S))
    print(pop(S))
    print(pop(S))