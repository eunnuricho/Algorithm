# M, N = map(int, input().split())
#
# for i in range(M, N + 1):
#     if i != 1:
#         for j in range(2, int(i ** 0.5) + 1):
#             _flag = True
#             if i % j == 0:
#                 _flag = False
#                 break
#     if _flag == True:
#         print(i)

x, y = map(int, input().split())

for i in range(x, y + 1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)
