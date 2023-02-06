arr = list(list(0 for _ in range(100)) for _ in range(100))

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            arr[j][k] = 1

ans = 0

for l in arr:
    ans += l.count(1)

print(ans)