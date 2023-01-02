def gcd(a, b):
    while b != 0:
        result = a % b
        a = b
        b = result
    return a

N = int(input())
nums = list(map(int, input().split()))

target = nums[0]

for i in range(1, N):
    num = gcd(target, nums[i])
    print('{}/{}'.format(target//num, nums[i]//num))