N = int(input())
nums = list(map(int, input().split()))
ans = N

for num in nums:
    cnt = 0

    if num == 1:
        ans -= 1

    for i in range(1, num):
        if num % i == 0:
            cnt += 1
            if cnt >= 2:
                ans -= 1
                break

print(ans)