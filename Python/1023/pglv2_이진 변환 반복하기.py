def solution(s):
    answer = []
    zero = 0
    cnt = 0

    while s != '1':
        new = ''
        cnt += 1
        for a in s:
            if a == '0':
                zero += 1
            else:
                new += a

        s = str(bin(int(len(new)))[2:])

    answer.append(cnt)
    answer.append(zero)

    return answer