N = int(input())

def solution(num, i):
    global  N
    if num % i == 0:
        N = N // i
        print(i)
        solution(N, i)
    else:
        return

#1이면 아무것도 출력하지 않음
if N != 1:
    for i in range(2, N + 1):
        #약수인지 확인
        if N % i == 0:
            #소수인지 확인
            for j in range(2, i):
                _flag = True
                if i % j == 0:
                    _flag = False
                    break
            solution(N, i)


# N = int(input())
# i = 2
# while N != 1:
#     if N % i == 0:
#         N = N // i
#         print(i)
#     else:
#         i += 1