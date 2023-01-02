#버블 정렬
N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

for i in range(N - 1):
    for j in range(N - 1, i, -1):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]

for k in range(N):
    print(arr[k])