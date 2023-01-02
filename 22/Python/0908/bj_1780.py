def cut(x, y, n):
    check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        cut(x + (k * n // 3), y + (l * n // 3), n // 3)
                return

    if check == -1:
        ans[0] += 1

    elif check == 0:
        ans[1] += 1

    else:
        ans[2] += 1

import sys
input = sys.stdin.readline

N = int(input())
paper = list(list(map(int, input().split())) for _ in range(N))
ans = [0] * 3

cut(0, 0, N)

print(*ans, sep='\n')