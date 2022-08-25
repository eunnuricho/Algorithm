def pado(N):
    arr = [0] * 101
    arr[1], arr[2], arr[3], arr[4], arr[5] = 1, 1, 1, 2, 2

    for i in range(6, N + 1):
        arr[i] = arr[i - 1] + arr[i - 5]

    return(arr[N])


T = int(input())
for _ in range(T):
    print(pado(int(input())))