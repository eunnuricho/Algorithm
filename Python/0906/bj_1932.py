n = int(input())
triangle = list(list(map(int, input().split())) for _ in range(n))

# _sum = triangle[0][0]
# idx = 0
#
# for i in range(1, n):
#     if triangle[i][idx] >= triangle[i][idx + 1]:
#         _sum += triangle[i][idx]
#     else:
#         _sum += triangle[i][idx + 1]
#         idx += 1
#
# print(_sum)

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
        else:
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

print(max(triangle[n - 1]))
