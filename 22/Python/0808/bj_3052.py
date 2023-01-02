nums = []

for i in range(10):
    nums.append(int(input()) % 42)

arr = set(nums)
print(len(arr))

#반복문
# for i in range(10):
#     if int(input()) % 42 not in nums:
#         nums.append(int(input()) % 42)
#
# print(len(nums))