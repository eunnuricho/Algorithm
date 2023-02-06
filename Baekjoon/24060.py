def msort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) + 1) // 2

    arr1 = msort(arr[:mid])
    arr2 = msort(arr[mid:])

    tmp = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            tmp.append(arr1[i])
            ans.append(arr1[i])
            i += 1
        else:
            tmp.append(arr2[j])
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        tmp.append(arr1[i])
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        tmp.append(arr2[j])
        ans.append(arr2[j])
        j += 1

    return tmp

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = []
msort(A)

if len(ans) >= K:
    print(ans[K - 1])
else:
    print(-1)