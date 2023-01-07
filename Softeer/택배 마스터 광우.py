import sys
from itertools import permutations

def work(arr):
    global ans
    total = 0
    cnt = 0

    for i in range(K):
        weight = 0

        while True:
            weight += arr[cnt]
            cnt = (cnt + 1) % N
            if weight + arr[cnt] > M:
                break

        total += weight

    if total < ans:
        ans = total


N, M, K = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

rails = list(permutations(weights, N))
ans = 987654321

for rail in rails:
    work(rail)

print(ans)