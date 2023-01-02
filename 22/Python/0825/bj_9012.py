T = int(input())

for _ in range(T):
    letters = list(input())
    stack = []

    for letter in letters:
        if letter == '(':
            stack.append(letter)
        elif letter == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break

    else:
        print('NO') if stack else print('YES')