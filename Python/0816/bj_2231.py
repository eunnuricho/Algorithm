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

# # 분해합
# def cal_num(num):
#     num_sum = 0
#     temp = num
#     while temp:
#         temp, n = divmod(temp, 10)
#         num_sum += n
#     if num + num_sum == N:
#         return num
#     return 0
#
# N = int(input())
# result = 0
# for num in range(max(0,N-100), N):
#     result = cal_num(num)
#     if result:
#         break
#
# print(result)
