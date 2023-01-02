N = int(input())
nums = list(map(int, input().split()))

#반복문
max = -1000001
min = 1000001

for i in range(N):
    if nums[i] > max:
        max = nums[i]
    if nums[i] < min:
        min = nums[i]

print(min, max, sep=' ')

#min, max
#
# max = max(nums)
# min = min(nums)
#
# print(min, max, sep=' ')

#sort
# nums.sort()
# print(nums[0], nums[-1], sep=' ')