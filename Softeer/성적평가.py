# import sys
#
# N = int(sys.stdin.readline())
#
# result = []
#
# for tc in range(3):
#     scores = list(map(int, sys.stdin.readline().split()))
#     result.append(scores)
#
# final = []
#
# for i in range(N):
#     total = 0
#     for j in range(3):
#         total += result[j][i]
#     final.append(total)
#
# result.append(final)
#
# for k in range(4):
#     ans = ''
#     tmp = sorted(result[k])
#     tmp.reverse()
#
#     for l in range(N):
#         target = result[k][l]
#         place = 0
#         tied = 0
#
#         for t in tmp:
#             if t > target:
#                 place += 1
#             elif t == target:
#                 tied += 1
#                 if tied < 2:
#                     place += 1
#                 else:
#                     break
#             else:
#                 break
#         ans += str(place) + ' '
#     print(ans)

import sys

N = int(sys.stdin.readline())

result = [[0 for _ in range(N)] for _ in range(4)]

for tc in range(3):
    scores = list(map(int, sys.stdin.readline().split()))

    for s in range(N):
        result[tc][s] = scores[s]
        result[3][s] += scores[s]

for k in range(4):
    ans = ''
    tmp = sorted(result[k], reverse = True)

    for l in range(N):
        target = result[k][l]
        place = tmp.index(target) + 1
        ans += str(place) + ' '
    print(ans)