N, M, V = map(int, input().split())

nodes = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    nodes[a][b] = nodes[b][a] =1

visited = [0] * (N + 1)

def dfs(V):
    visited[V] = 1
    print(V, end=' ')
    for i in range(1, N + 1):
        if visited[i] == 0 and nodes[V][i] == 1:
            dfs(i)

def bfs(V):
    _que = [V]
    visited[V] = 0
    while _que:
        V = _que.pop(0)
        print(V, end=' ')
        for i in range(1, N + 1):
            if visited[i] == 1 and nodes[V][i] == 1:
                _que.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)