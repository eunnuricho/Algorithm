N = int(input())
nums = list(map(int, input().split()))

stack = [0]     # nums 배열의 인덱스를 넣어 확인 (0부터 시작)
ans = [-1 for _ in range(N)]    # 정답 출력할 리스트

for i in range(1, N):
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)

print(*ans)