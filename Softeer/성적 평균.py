import sys

N, K = map(int, sys.stdin.readline().split())

grades = list(map(int, sys.stdin.readline().split()))

for _ in range(K):
    st, ed = map(int, sys.stdin.readline().split())
    mean = sum(grades[st - 1 : ed]) / (ed - st + 1)
    print(f'{mean : .2f}')