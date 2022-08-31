import sys

input = sys.stdin.readline

while True:
    letters = input().rstrip()

    if letters == '.':
        break

    stack = []

    for letter in letters:
        if letter == '(' or letter == '[':  # 여는 괄호 . 담음.
            stack.append(letter)

        elif not stack:
            if letter == ')' or letter == ']':  # 스택에 아무것도 없는데 닫는 괄호
                stack.append(letter)
                break

        elif letter == ')' or letter == ']':  # 스택이 있고 닫는 괄호
            if letter == ')' and stack[-1] == '(':  # 열, 닫 짝이 맞음
                stack.pop()
            elif letter == ']' and stack[-1] == '[':
                stack.pop()
            else:  # 짝이 안 맞음
                stack.append(letter)
                break

    print('no') if stack else print('yes')
