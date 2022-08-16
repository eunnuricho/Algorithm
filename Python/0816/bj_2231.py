#n이 N의 생성자인지 확인 후 리턴해주는 함수
def solution(n):
    _sum = n
    nums = list(str(n))

    for i in range(len(nums)):
        _sum += int(nums[i])
    if _sum == N:
        return n
    return 0

N = int(input())

nums = list(range(1, N + 1))
ans = 0

for num in nums:
    if solution(num):
        ans = solution(num)
        break

print(ans)