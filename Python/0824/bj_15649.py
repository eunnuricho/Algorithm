def seq(arr, nums):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(len(nums)):
        if nums[i] not in arr:
            arr.append(nums[i])
            seq(arr, nums)
            arr.pop(-1)
        else:
            continue

N, M = map(int, input().split())
nums = list(range(1, N + 1))
arr = []

seq(arr, nums)