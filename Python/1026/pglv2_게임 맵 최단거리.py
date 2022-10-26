from collections import deque

def solution(maps):
    answer = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def search(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dr[i]
                ny = y + dc[i]

                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                    continue

                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        return maps[len(maps) - 1][len(maps[0]) - 1]

    answer = search(0, 0)

    return answer if answer != 1 else -1