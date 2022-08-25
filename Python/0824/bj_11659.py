import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

arr = [0]

for i in range(N):
    tmp = arr[-1] + nums[i]
    arr.append(tmp)

print(arr)

for j in range(M):
    a, b = map(int, input().split())
    print(arr[b] - arr[a - 1])