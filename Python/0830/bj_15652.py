def seq(arr, nums):  # 중복 있어도 되는
    if len(arr) == M:
        print(*arr)
        return

    for i in range(len(nums)):
        if not arr:
            arr.append(nums[i])
        elif nums[i] >= arr[-1]:    # 마지막 숫자보다 같거나 클 때만(비내림차순)
            arr.append(nums[i])
        else:                       # 확인
            continue
        seq(arr, nums)
        arr.pop()


N, M = map(int, input().split())
nums = list(range(1, N + 1))
arr = []

seq(arr, nums)
