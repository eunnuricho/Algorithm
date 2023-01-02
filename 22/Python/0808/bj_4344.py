T = int(input())

for tc in range(T):
    arr = list(map(int, input().split()))
    mean = sum(arr[1:]) / arr[0]
    cnt = 0

    for i in arr[1:]:
        if i > mean:
            cnt += 1

    print(f'{(cnt / arr[0]) * 100:.3f}%')