import sys

N, M, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = [[0] * M for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            if i == 0 or j == 0:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + 1

            ans = max(ans, C[i][j])

print(ans)