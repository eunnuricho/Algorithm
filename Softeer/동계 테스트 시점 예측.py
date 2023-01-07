import sys
from collections import deque

def melt():
    queue = deque([[0, 0]])
    visited[0][0] = 1

    while queue:
        c, r = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < M and 0 <= nc < N:
                if arjeplog[nc][nr]:
                    visited[nc][nr] += 1
                elif not visited[nc][nr]:
                    queue.append([nc, nr])
                    visited[nc][nr] = 1

    for j in range(N):
        for k in range(M):
            if visited[j][k] >= 2:
                arjeplog[j][k] = 0


N, M = map(int, sys.stdin.readline().split())
arjeplog = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

cnt = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while arjeplog.count([0] * M) != N:
    visited = list([0] * M for _ in range(N))
    melt()
    cnt += 1

print(cnt)