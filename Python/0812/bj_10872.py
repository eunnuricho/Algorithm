def Fac(num):
    if num > 0:
        return num * Fac(num - 1)
    return 1

N = int(input())
print(Fac(N))

#for문

# N = int(input())
# ans = 1
#
# for i in range(1, N):
#     ans *= i
#
# print(ans)