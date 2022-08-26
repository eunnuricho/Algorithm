def seq(arr, nums):         # 중복 있어도 되는
    if len(arr) == M:
        print(*arr)
        return

    for i in range(len(nums)):      # for문 순서에 따라 사전 순이 됨
        arr.append(nums[i])
        seq(arr, nums)
        arr.pop()

N, M = map(int, input().split())
nums = list(range(1, N + 1))
arr = []

seq(arr, nums)