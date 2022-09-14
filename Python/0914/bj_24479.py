import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(V, cnt):
    visited[V - 1] = cnt
    nodes[V].sort()

    for i in range(1, N + 1):
        if visited[i - 1] == 0 and nodes[V][i] == 1:
            dfs(i, cnt + 1)


N, M, R = map(int, input().split())

nodes = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N)

for i in range(M):
    a, b = map(int, input().split())
    nodes[a][b] = nodes[b][a] = 1

dfs(R, 1)

print(*visited, sep='\n')
