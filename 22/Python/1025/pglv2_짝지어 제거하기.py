def solution(s):
    answer = -1
    stack = ['0']

    for a in s:
        if a != stack[-1]:
            stack.append(a)
        else:
            stack.pop()

    if len(stack) > 1:
        answer = 0
    else:
        answer = 1

    return answer