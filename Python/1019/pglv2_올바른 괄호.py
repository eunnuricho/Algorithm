def solution(s):
    answer = True
    stack = []

    arr = s.split()
    for a in arr:
        if a == '(':
            stack.append(a)
        else:
            if stack:
                stack.pop(0)
            else:
                answer = False
                break
    if arr:
        answer = False

    return answer

# def solution(s):
#     answer = True
#     stack = []
#
#     for a in s:
#         if a == '(':
#             stack.append(a)
#         else:
#             if stack:
#                 stack.pop()
#             else:
#                 answer = False
#                 break
#     if stack:
#         answer = False
#
#     return answer