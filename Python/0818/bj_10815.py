import sys

N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

ans = [0] * M

for i in range(M):
    if nums[i] in cards:
        ans[i] += 1

print(*ans)

# 이진 탐색
# cards.sort()
#
# for num in nums:
#     low, high = 0, N - 1  # cards의 이진 탐색 index
#     exist = False
#     while low <= high:
#         mid = (low + high) // 2
#         if cards[mid] > num:  # 중간 값보다 작다면
#             high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
#         elif cards[mid] < num:  # 중간 값보다 크다면
#             low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
#         else:
#             exist = True
#             break
#     print(1 if exist else 0, end=' ')
