# def Fibo(n):
#     if n <= 1:
#         return n
#     return Fibo(n - 1) + Fibo(n - 2)
#
# n = int(input())
# print(Fibo(n))

def Fibo(num1, num2):
    global cnt
    if n == 0:
        return 0
    if cnt == n:
        return num2
    cnt += 1
    return Fibo(num2, num1 + num2)

n = int(input())
cnt = 1
print(Fibo(0, 1))

#for문
# n = int(input())
# Fibo = [0, 1]
# for i in range(2, n + 1):
#     num = Fibo[i - 1] + Fibo[i - 2]
#     Fibo.append(num)
# print(Fibo[n])