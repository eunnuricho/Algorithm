N = int(input())

ans = 0
row = [0] * N       # 퀸이 놓여진 행을 체크

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # 같은 열에 있거나 대각선으로 만나는 경우
            return False
    return True

def n_queens(x):
    global ans
    if x == N:
        ans += 1
        return

    else:
        for i in range(N):
            # [x, i] -> 행, 열
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

n_queens(0)
print(ans)
