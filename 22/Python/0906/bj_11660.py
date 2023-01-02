import sys
input = sys.stdin.readline

# N, M = map(int, input().split())
# nums = list(list(map(int, input().split())) for _ in range(N))
#
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     sum = 0
#     for j in range(x1 - 1, x2):
#         for k in range(y1 - 1, y2):
#             sum += nums[j][k]
#     print(sum)

n, m = map(int, input().split())

numbers = [[0] * (n + 1)]

for _ in range(n):
    nums = [0] + [int(x) for x in input().split()]
    numbers.append(nums)

# prefix sum 행렬 만들기

# 1. 행 별로 더하기
for i in range(1, n + 1):
    for j in range(1, n):
        numbers[i][j + 1] += numbers[i][j]

# 2. 열 별로 더하기
for j in range(1, n + 1):
    for i in range(1, n):
        numbers[i + 1][j] += numbers[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # (x1, y1)에서 (x2, y2)까지의 합
    # p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]
    print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])
