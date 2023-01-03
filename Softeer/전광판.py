# import sys
#
# T = int(sys.stdin.readline())
#
# lights = {'0': [1, 1, 1, 0, 1, 1, 1], '1': [0, 0, 1, 0, 0, 1, 0], '2': [1, 0, 1, 1, 1, 0, 1],
#           '3': [1, 0, 1, 1, 0, 1, 1],
#           '4': [0, 1, 1, 1, 0, 1, 0], '5': [1, 1, 0, 1, 0, 1, 1], '6': [1, 1, 0, 1, 1, 1, 1],
#           '7': [1, 1, 1, 0, 0, 1, 0],
#           '8': [1, 1, 1, 1, 1, 1, 1], '9': [1, 1, 1, 1, 0, 1, 0]}

# for tc in range(T):
#     curr, target = sys.stdin.readline().split()
#     curr_lst = list(curr)
#     target_lst = list(target)
#     ans = 0
#
#     if len(target) > len(curr):
#         add = len(target) - len(curr)
#
#         for i in range(add):
#             ans += sum(lights[target_lst[i]])
#
#         target = target[add:]
#
#         for j in range(add, len(curr)):
#             a, b, = lights[curr_lst[j]], lights[target_lst[j]]
#
#             for k in range(7):
#                 if a[k] != b[k]:
#                     ans += 1
#
#     elif len(target) < len(curr):
#         delete = len(curr) - len(target)
#
#         for i in range(delete):
#             ans += sum(lights[curr_lst[i]])
#
#         curr = curr[delete:]
#
#         for j in range(delete, len(target)):
#             a, b, = lights[curr_lst[j]], lights[target_lst[j]]
#
#             for k in range(7):
#                 if a[k] != b[k]:
#                     ans += 1
#
#     else:
#         for j in range(len(curr)):
#             a, b, = lights[curr_lst[j]], lights[target_lst[j]]
#
#             for k in range(7):
#                 if a[k] != b[k]:
#                     ans += 1
#
#     print(ans)

import sys

T = int(sys.stdin.readline())

lights = {'0' : [1, 1, 1, 0, 1, 1, 1], '1': [0, 0, 1, 0, 0, 1, 0], '2': [1, 0, 1, 1, 1, 0, 1], '3': [1, 0, 1, 1, 0, 1, 1],
'4': [0, 1, 1, 1, 0, 1, 0], '5': [1, 1, 0, 1, 0, 1, 1], '6': [1, 1, 0, 1, 1, 1, 1], '7': [1, 1, 1, 0, 0, 1, 0],
'8': [1, 1, 1, 1, 1, 1, 1], '9': [1, 1, 1, 1, 0, 1, 1], ' ': [0, 0, 0, 0, 0, 0, 0]}

for tc in range(T):
    curr, target = sys.stdin.readline().split()
    curr = (5 - len(curr)) * ' ' + curr
    target = (5 - len(target)) * ' ' + target
    ans = 0

    for i in range(5):
        for j in range(7):
            ans += (lights[curr[i]][j] != lights[target[i]][j])

    print(ans)