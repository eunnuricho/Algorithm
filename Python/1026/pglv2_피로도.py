from itertools import permutations

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    arr = list(permutations(dungeons, n))

    def game(cnt, a, k):
        nonlocal answer
        for i in range(n):
            if k >= a[i][0]:
                cnt += 1
                k -= a[i][1]
        if cnt > answer:
            answer = cnt

    for a in arr:
        cnt = 0
        game(cnt, a, k)

    return answer