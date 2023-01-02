#생성자가 있는 숫자를 리턴해주는 함수
def solution(n):
    nums = list(str(n))

    for i in range(len(nums)):
        n += int(nums[i])
    if n <= 10000:
        arr.append(n)

    return n

nums = list(range(1, 10001))
arr = []

for num in nums:
    solution(num)

#생성자가 있는 숫자를 모은 리스트에서 중복을 제거한 후 전체 리스트에서 제거
for a in set(arr):
    nums.remove(a)

for self_num in nums:
    print(self_num)