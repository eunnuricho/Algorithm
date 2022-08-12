def Fac(num):
    ans = 1
    if num > 0:
        ans = num * Fac(num - 1)
    return ans

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