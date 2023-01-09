import sys

N, K = map(int, sys.stdin.readline().split())
line = list(sys.stdin.readline())
used = [1] * N

cnt = 0
for i in range(N):
    if line[i] == 'H':
        for j in range(i - K, i + K + 1):
            if 0 <= j < N:
                if line[j] == 'P' and used[j]:
                    used[j] = 0
                    cnt += 1
                    break

print(cnt)