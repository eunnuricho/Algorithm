import sys

N = int(sys.stdin.readline())

result = []

for tc in range(N):
    p1, p2, p3 = map(int, sys.stdin.readline().split())
    result.append([p1, p2, p3])

final = []

for i in range(3):
    total = 0
    for j in range(N):
        total += result[j][i]
    final.append(total)

result.append(final)

for k in range(4):
    ans = []
    for l in range(N):
        target = result[k][l]
        place = 0
        tied = False
        for m in range(N):
            if result[k][m] > target:
                place += 1
            elif result[k][m] == target:
                if not tied:
                    place += 1
                    tied = True
        ans.append(place)
    print(*ans)