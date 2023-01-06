import sys

N = int(sys.stdin.readline())

lines = []
move = []

for _ in range(N - 1):
    arr = list(map(int, sys.stdin.readline().split()))
    tmp1 = []
    tmp2 = []
    for i in range(len(arr)):
        if i < 2:
            tmp1.append(arr[i])
        else:
            tmp2.append(arr[i])

    lines.append(tmp1)
    move.append(tmp2)

final_a, final_b = map(int, sys.stdin.readline().split())

lines.append([final_a, final_b])

# print(lines)
# print(move)

dp_a = [lines[0][0]] + ([0] * (N - 1))
dp_b = [lines[0][1]] + ([0] * (N - 1))

for j in range(len(lines) - 1):
    dp_a[j + 1] = min(lines[j + 1][0], move[j][0] + lines[j + 1][1]) + dp_a[j]
    dp_b[j + 1] = min(lines[j + 1][1], move[j][1] + lines[j + 1][0]) + dp_b[j]

# print(dp_a)
# print(dp_b)

print(min(dp_a[N - 1], dp_b[N - 1]))