import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
waybackhome = list(list(sys.stdin.readline().rstrip()) for _ in range(R))

def spread():
    global rain
    tmp = []

    for r, c in rain:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if waybackhome[nr][nc] == '.':
                    waybackhome[nr][nc] = '*'
                    tmp.append((nr, nc))
    rain = list(set(rain + tmp))


def bfs(r, c):
    tmp = 0
    visited[r][c] = 1
    spread()
    queue = deque([[r, c, 0]])

    while queue:
        r, c, cnt = queue.popleft()
        if tmp != cnt:
            spread()

        tmp = cnt

        for l in range(4):
            nr = r + dr[l]
            nc = c + dc[l]
            if 0 <= nr < R and 0 <= nc < C:
                if waybackhome[nr][nc] == 'H':
                    return cnt + 1

                if waybackhome[nr][nc] == '.' and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append([nr, nc, cnt + 1])
    return "FAIL"


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[0] * C for _ in range(R)]

curr_r, curr_c = 0, 0
rain = []

for i in range(R):
    for j in range(C):
        if waybackhome[i][j] == 'W':
            curr_r, curr_c = i, j

        if waybackhome[i][j] == '*':
            rain.append((i, j))

print(bfs(curr_r, curr_c))