# def solution(n, times):
#     answer = 0
#     lines = []
#
#     for i in range(times):
#         lines.append(times[i])
#
#     lines.sort()
#     while len(lines) < n:
#         while left < right:
#             left = 0
#             right = len(lines) - 1
#             mid = (lines[left] + lines[right]) // 2
#
#     # 0, 0, 7, 10, 14 + 7, 20 + 10, 21 + 7
#
#     return answer