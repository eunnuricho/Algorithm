def fib(n):     #top-down
    global cnt1
    cnt1 += 1

    if n == 1 or n == 2:
        cnt1 -= 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def dp(n):      #bottom-up
    global cnt2

    _dp = [0] * (n + 1)
    _dp[1], _dp[2] = 1, 1

    for i in range(3, n + 1):
        cnt2 += 1
        _dp[i] = _dp[i - 1] + _dp[i - 2]
    return cnt2


N = int(input())
cnt1, cnt2 = 1, 0

fib(N)
dp(N)

print(cnt1, cnt2)


# ??
#
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# def fibonacci(n):
#     dp = [0] * (n + 1)
#     dp[1], dp[2] = 1, 1
#     cnt2 = 0
#     for i in range(3, n + 1):
#         cnt2 += 1
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return cnt2
#
#
# n = int(input())
# print(fib(n), fibonacci(n))