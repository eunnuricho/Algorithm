import math

N, K = map(int, input().split())
print(math.comb(N, K))


# 팩토리얼 - 재귀
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
#
# n, k = map(int, input().split())
# print(factorial(n) // (factorial(k) * factorial(n - k)))

# 반복문
# def factorial(n):
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
