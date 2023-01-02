def solution(num):
    if num < 100:
        return True

    else:
        arr = list(str(num))
        dif = int(arr[0]) - int(arr[1])

        for i in range(len(arr) - 1):
            if int(arr[i]) - int(arr[i + 1]) != dif:
                return False
        return True

N = int(input())
ans = 0

for i in range(1, N + 1):
    if solution(i):
        ans += 1

print(ans)