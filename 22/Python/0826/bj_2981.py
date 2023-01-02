# import sys
# input = sys.stdin.readline
#
# N = int(input())
# nums = sorted(int(input()) for _ in range(N))
#
#
# tmp = nums[0]
# while True:
#
#     for i in range(1, N):
#         nums[i] %= tmp
#         nums.sort()
#         print(nums)
#
#     if 0 in nums:
#         break
#
# print(nums)

# 최대공약수(유클리드 호제법)
def gcd(a, b):
    num = b
    div = a
    result = num % div

    while result != 0:
        num = div
        div = result
        result = num % div
    return div

N = int(input())
nums = sorted(int(input()) for _ in range(N))

arr = []

for i in range(1, N):
    arr.append(nums[i] - nums[i - 1])

tmp = arr[0]
for j in range(1, len(arr)):
    tmp = gcd(tmp, arr[j])

ans = set()
for k in range(2, int(tmp ** 0.5) + 1):
    if tmp % k == 0:
        ans.add(k)
        ans.add(tmp // k)

ans.add(tmp)
print(*sorted(list(ans)))
