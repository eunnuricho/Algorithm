import sys

K, P, N = list(map(int, sys.stdin.readline().split()))

def virus(x, y):
    if y == 1:
        return x

    half = virus(x, y // 2)

    if y % 2:
        return (half * half * x) % 1000000007

    else:
        return (half * half) % 1000000007

print(K * virus(P, (10 * N)) % 1000000007)