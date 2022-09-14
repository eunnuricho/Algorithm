import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(V):
    global cnt
    visited[V] = cnt
    cnt += 1
    nodes[V].sort()

    for node in nodes[V]:
        if visited[node] == 0:
            dfs(node)


N, M, R = map(int, input().split())

nodes = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

cnt = 1
dfs(R)

visited.pop(0)
print(*visited, sep='\n')
