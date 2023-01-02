N, M = map(int, input().split())

_dict = {}
ans = 0

for i in range(N):
    _dict[input()] = 0

for j in range(M):
    if input() in _dict:
        ans += 1

print(ans)