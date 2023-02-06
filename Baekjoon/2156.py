n = int(input())
wine = [0] * n

for i in range(n):
    wine[i] = int(input())

dp = [0] * n

for j in range(n):
    if j == 0:
        dp[j] = wine[j]
    elif j == 1:
        dp[j] = wine[j - 1] + wine[j]
    elif j == 2:
        dp[j] = max(wine[j - 2] + wine[j], wine[j - 1] + wine[j], dp[j - 1])
    else:
        dp[j] = max(wine[j] + dp[j - 2], wine[j - 1] + wine[j] + dp[j - 3], dp[j - 1])

print(max(dp))
