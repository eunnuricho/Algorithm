N, K = map(int, input().split())
nums = []
_cnt = 0

for _ in range(N):
    n = int(input())
    if n > K:
        break

    elif n == K:
        _cnt = 1
        break

    else:
        nums.append(n)

nums.sort(reverse=True)

if not _cnt == 1:
    for i in range(len(nums)):
        if nums[i] > K:
            continue
        if K == 0:
            break
        _cnt += (K // nums[i])
        K %= nums[i]

print(_cnt)