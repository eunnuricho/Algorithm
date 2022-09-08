def dfs(a, b):
    global cnt
    visited[a][b] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for k in range(4):
            nr = a + dr[k]
            nc = b + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 and danji[nr][nc] == 1:
                    cnt += 1
                    dfs(nr, nc)
    return cnt

N = int(input())
danji = list(list(map(int, input())) for _ in range(N))
visited = [[0] * N for _ in range(N)]
cnt = 1
lst = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and danji[i][j] == 1:
            lst.append(dfs(i, j))
            cnt = 1

lst.sort()
print(len(lst))
for i in range(len(lst)):
    print(lst[i], end='\n')