def cut(x, y, n):
    global white, blue
    check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:        # 하나라도 같은 색이 아닐 때 다시 4등분
                cut(x, y, n // 2)                       # 1사분면
                cut(x, y + n // 2, n // 2)              # 2사분면
                cut(x + n // 2, y, n // 2)              # 3사분면
                cut(x + n // 2, y + n // 2, n // 2)     # 4사분면
                return

    if check == 0:      # 모두 흰색
        white += 1
        return
    else:               # 모두 파란색
        blue += 1
        return


import sys
input = sys.stdin.readline

N = int(input())
paper = list(list(map(int, input().split())) for _ in range(N))

white = 0
blue = 0

cut(0, 0, N)
print(white)
print(blue)