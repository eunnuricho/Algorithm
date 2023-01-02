import sys

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for k in range(N):
    print(arr[k])