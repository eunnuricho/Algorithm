def solution(n, computers):
    answer = 0

    def cal(idx, cnt):
        for j in range(idx, n):
            if computers[idx][j] and j != idx:
                cnt += 1
                cal(idx + 1, cnt)
        return cnt

    for k in range(n):
        print(cal(k, 0))

    return answer