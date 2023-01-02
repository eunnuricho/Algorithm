N = int(input())
arr = sorted(map(int, input().split()))

for i in range(1, N):
    arr[i] = arr[i - 1] + arr[i]

print(sum(arr))