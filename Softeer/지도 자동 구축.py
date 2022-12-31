import sys

ans = 2
N = int(sys.stdin.readline())

for i in range(N):
    ans *= 2
    ans -= 1

print(ans ** 2)