# def solution(n, edge):
#     answer = 0
#     arr = [[0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(len(edge)):
#         arr[edge[i][0] - 1][edge[i][1] - 1] = 1
#         arr[edge[i][1] - 1][edge[i][0] - 1] = 1
#
#     ans = [0 for _ in range(n)]
#     visited = [0 for _ in range(n)]
#     cnt = 0
#     tmp = [0]
#
#     while tmp:
#         cnt += 1
#         target = tmp.pop()
#         for j in range(1, n):
#             if arr[target][j] != 0 and not visited[j]:
#                 visited[j] = 1
#                 ans[j] = cnt
#                 tmp.append(j)
#
#     print(ans)
#
#     return answer