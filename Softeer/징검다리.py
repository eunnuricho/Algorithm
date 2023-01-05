import sys

N = int(sys.stdin.readline())

rocks = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if rocks[i] > rocks[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))