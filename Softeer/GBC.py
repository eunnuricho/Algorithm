import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

std = deque()

for _ in range(N):
    length, speed = map(int, sys.stdin.readline().split())
    std.append((length, speed))

test = deque()

for _ in range(M):
    length, speed = map(int, sys.stdin.readline().split())
    test.append((length, speed))

off = 0
idx = 0

while test:
    leng, std_spd = std.popleft()
    tested, speed = test.popleft()
    left = 0
    if tested > leng:
        left = tested - leng
        test.appendleft((left, speed))
    if leng > tested:
        left = leng - tested
        std.appendleft((left, std_spd))
    if std_spd < speed and speed - std_spd > off:
        off = speed - std_spd

print(off)