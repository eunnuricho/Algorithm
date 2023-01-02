# while True:
#     N = int(input())
#     arr = []
#     cnt = 0
#     for i in range(N, 2 * N):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 continue
#             else:
#                 cnt += 1
#         arr.append(cnt)
#
#     if N == 0:
#         print(*arr, sep='\n')
#         break


while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, (2 * n) + 1):
        _flag = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                _flag = False
                break
        if _flag == True and i != 1:
            cnt += 1

    print(cnt)