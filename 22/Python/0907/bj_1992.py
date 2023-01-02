def compress(x, y, n):
    check = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n //= 2
        compress(x, y, n)
        compress(x, y + n, n)
        compress(x + n, y, n)
        compress(x + n, y + n, n)
        print(")", end='')

    elif check == 1:
        print(1, end='')

    else:
        print(0, end='')


import sys
input = sys.stdin.readline

N = int(input())
board = list(list(map(int, input().strip())) for _ in range(N))

# print(board)
compress(0, 0, N)