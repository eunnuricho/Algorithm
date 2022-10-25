def solution(arr):
    answer = 0
    target = max(arr)
    multi = 1

    while True:
        tmp = target * multi
        cnt = 0
        for a in arr:
            if tmp % a == 0:
                cnt += 1
        if cnt == len(arr):
            answer = tmp
            break
        else:
            multi += 1

    return answer