def cal(_idx):
    global K, _cnt

    _cnt += (K // nums[_idx])
    K -= (nums[_idx] * (K // nums[_idx]))

    if K == 0:
        return _cnt

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
        if cal(i):
            break

print(_cnt)