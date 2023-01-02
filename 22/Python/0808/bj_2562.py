max = 0
max_idx = 0

for i in range(1, 10):
    n = int(input())
    if n > max:
        max = n
        max_idx = i

print("""{}
{}""".format(max, max_idx))

#list1

# nums = []
# for _ in range(9):
#     i = int(input())
#     nums.append(i)
#
# print("""{}
# {}""".format(max(nums)), nums.index(max(nums)) + 1)

#list2

# nums = [int(input()) for _ in range(9)]
#
# print("""{}
# {}""".format(max(nums)), nums.index(max(nums)) + 1)