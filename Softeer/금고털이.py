import sys

W, N = map(int, sys.stdin.readline().split())

jewels = []

for _ in range(N):
    weight, price = map(int, sys.stdin.readline().split())
    jewels.append([weight, price])

ans = 0
jewels.sort(key = lambda x: x[1], reverse = True)

# print(jewels)

idx = 0
while W != 0:
    if jewels[idx][0] and jewels[idx][0] <= W:
        W -= jewels[idx][0]
        ans += jewels[idx][0] * jewels[idx][1]
        jewels[idx][0] = 0
    elif jewels[idx][0] and jewels[idx][0] > W:
        ans += W * jewels[idx][1]
        W = 0
        jewels[idx][0] = 0
    idx += 1

print(ans)