def solution(n):
    answer = n + 1
    while True:
        if str(bin(n))[2:].count('1') == str(bin(answer))[2:].count('1'):
            break
        else:
            answer += 1
    return answer