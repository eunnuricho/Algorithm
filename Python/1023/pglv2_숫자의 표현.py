def solution(n):
    answer = 0

    nums = list(range(1, n + 1))

    for i in range(n):
        tmp = 0
        for j in range(i, n):
            tmp += nums[j]
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break

    return answer