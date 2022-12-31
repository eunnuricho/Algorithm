import sys
from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(road, a, b):
    n = len(road)
    queue = deque()
    queue.append((a, b))
    road[a][b] = 0
    cnt = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if road[nr][nc] == 1:
                road[nr][nc] = 0
                queue.append((nr,nc))
                cnt += 1

    return cnt

N = int(sys.stdin.readline())

road = []

for _ in range(N):
    road.append(list(map(int, sys.stdin.readline().strip())))

obstacles = []

for i in range(N):
    for j in range(N):
        if road[i][j] == 1:
            obstacles.append(bfs(road, i, j))

print(len(obstacles))

obstacles.sort()

for obs in obstacles:
    print(obs)