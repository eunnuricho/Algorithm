import math

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N - 1)

T = int(input())
for _ in range(T):
    west, east = map(int, input().split())
    print(math.comb(east, west))
    # print(factorial(east) // (factorial(east - west) * factorial(west)))