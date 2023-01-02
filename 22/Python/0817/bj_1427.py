N = input()
arr = [0] * len(N)

for i in range(len(N)):
    arr[i] += int(N[i])

arr.sort(reverse=True)

print(*arr, sep='')