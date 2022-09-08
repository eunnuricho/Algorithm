def dfs(V):
    global cnt
    visited[V] = 1
    cnt += 1
    for i in range(1, N + 1):
        if visited[i] == 0 and computers[V][i] == 1:
            dfs(i)

N = int(input())
M = int(input())
computers = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0

for i in range(M):
    a, b = map(int, input().split())
    computers[a][b] = computers[b][a] = 1

dfs(1)

print(cnt - 1)