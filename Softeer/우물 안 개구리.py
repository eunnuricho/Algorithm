import sys

N, M = map(int, sys.stdin.readline().split())

weights = [0] + list(map(int, sys.stdin.readline().split()))
community = [0] + ([1] * N)

for _ in range(M):
    p1, p2 = map(int, sys.stdin.readline().split())

    if weights[p1] < weights[p2]:
        community[p1] = 0

    if weights[p1] > weights[p2]:
        community[p2] = 0

    if weights[p1] == weights[p2]:
        community[p1], community[p2] = 0, 0

print(sum(community))