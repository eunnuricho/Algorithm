import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([])

for i in range(1, n + 1):
    q.append(i)

ans = []
while len(q) > 0:
    for i in range(k - 1):
        q.append(q[0])
        q.popleft()
    ans.append(q.popleft())

print('<', end='')
print(*ans, sep=', ', end='')
print('>', end='')