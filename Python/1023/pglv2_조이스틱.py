# def solution(name):
#     answer = 0
#     arr = list(name)
#     init = list('A' * len(name))
#     n = len(arr)
#
#     for idx in range(n):
#         if init[idx] != name[idx]:
#             tmp = min(abs(ord(init[idx]) - ord(name[idx])),
#                       abs(ord(init[idx]) - ord('A') + 1 + ord('Z') - ord(name[idx])))
#             answer += (tmp + 1)
#         else:
#             answer -= 1
#
#     return answer