def solution(n):
    answer = 0
    fibo = [0, 1]
    for i in range(2, n + 1):
        tmp = fibo[i -1] + fibo[i - 2]
        fibo.append(tmp % 1234567)

    answer = fibo[n]
    return answer