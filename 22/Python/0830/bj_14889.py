import sys
input = sys.stdin.readline

def cal(idx, cnt):
    global ans
    if cnt == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if select[i] and select[j]:
                    start += arr[i][j]
                elif not select [i] and not select[j]:
                    link += arr[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, N):
        if select[i]:
            continue
        select[i] = 1
        cal(i + 1, cnt + 1)
        select[i] = 0

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))

select = [0 for _ in range(N)]
ans = sys.maxsize

cal(0, 0)

print(ans)