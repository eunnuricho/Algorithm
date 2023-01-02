def seq(arr, nums):
    if len(arr) == M:
        print(*sorted(arr))     # 오름차순으로
        return

    for i in range(len(nums)):
        if nums[i] not in arr:
            arr.append(nums[i])
            seq(arr, nums[i + 1:])      # 중복 없이
            arr.pop()
        else:
            continue

N, M = map(int, input().split())
nums = list(range(1, N + 1))
arr = []

seq(arr, nums)