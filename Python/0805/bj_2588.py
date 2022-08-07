A = int(input())
B = input()

AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')


# A = int(input())
#
# B = input()
#
# for i in range(2, -1, -1):
#     print(A * int(B[i]))
#
# print(A * int(B))


# A = int(input())
#
# B = int(input())
#
# print(A * (B % 10))
#
# print(A * (B % 100 // 10))
#
# print(A * (B // 100))
#
# print(A * B)