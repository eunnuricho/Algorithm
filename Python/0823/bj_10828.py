import sys

N = int(sys.stdin.readline())
_stack = []

for i in range(N):
    _input = sys.stdin.readline().split()
    command = _input[0]

    if command == 'push':
        _stack.append(_input[1])

    elif command == 'pop':
        if len(_stack) == 0:
            print(-1)
        else:
            print(_stack.pop())

    elif command == 'size':
        print(len(_stack))

    elif command == 'empty':
        if len(_stack) == 0:
            print(1)
        else:
            print(0)

    elif command == 'top':
        if len(_stack) == 0:
            print(-1)
        else:
            print(_stack[-1])