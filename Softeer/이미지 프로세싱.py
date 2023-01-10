import sys

def color(r, c, new):
    stack = [[r, c]]
    curr = image[r][c]

    if curr != new:
        while stack:
            r, c = stack.pop()

            if 0 <= r < H and 0 <= c < W and image[r][c] == curr:
                image[r][c] = new

                for i in range(4):
                    stack.append([r + dr[i], c + dc[i]])


H, W = map(int, sys.stdin.readline().split())
image = list(list(map(int, sys.stdin.readline().split())) for _ in range(H))
Q = int(sys.stdin.readline())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(Q):
    r, c, new = map(int, sys.stdin.readline().split())
    color(r - 1, c - 1, new)

for img in image:
    print(*img)