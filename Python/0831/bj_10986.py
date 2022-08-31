N, M = map(int, input().split())
nums = list(map(int, input().split()))
ls = [0]
arr = [0]

cnt = 0
_sum = 0
for i in range(N):
    _sum += nums[i]
    ls.append(_sum)
    arr.append(_sum % M)

print(ls)
print(arr)
