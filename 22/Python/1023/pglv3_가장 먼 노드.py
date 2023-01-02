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

from collections import deque

def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n + 1)]

    for i in range(len(edge)):
        arr[edge[i][0]].append(edge[i][1])
        arr[edge[i][1]].append(edge[i][0])

    visited = [1, 1] + [0 for _ in range(n - 1)]
    tmp = deque([1])

    while tmp:
        target = tmp.popleft()
        for a in arr[target]:
            if not visited[a]:
                visited[a] = visited[target] + 1
                tmp.append(a)

    answer += visited.count(max(visited))

    return answer