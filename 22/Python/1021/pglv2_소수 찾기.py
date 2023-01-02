from itertools import permutations

def solution(numbers):
    answer = 0
    arr = []
    for num in numbers:
        arr.append(num)

    def isprime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    n = len(arr)
    target = []

    for i in range(1, n + 1):
        perm = list(permutations(arr, i))
        for j in range(len(perm)):
            tmp = int(''.join(perm[j]))
            if tmp not in target and tmp > 1:
                target.append(tmp)

    # print(target)

    for k in target:
        if isprime(k):
            answer += 1

    return answer


# from itertools import permutations
#
#
# def solution(numbers):
#     answer = 0
#     arr = []
#     for num in numbers:
#         arr.append(num)
#
#     def isprime(n):
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     n = len(arr)
#     target = set()
#
#     for i in range(1, n + 1):
#         perm = list(permutations(arr, i))
#         for j in range(len(perm)):
#             tmp = int(''.join(perm[j]))
#             if tmp > 1:
#                 target.add(tmp)
#
#     # print(target)
#
#     for k in target:
#         if isprime(k):
#             answer += 1
#
#     return answer

# 에라토스테네스의 체................