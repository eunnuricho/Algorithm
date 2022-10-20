def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def count(ans, cnt):
        if cnt == n:
            if ans == target:
                answer += 1
            return
        else:
            ans += numbers[cnt]
            count(ans, cnt + 1)
            ans -= numbers[cnt]
            count(ans, cnt + 1)

    count(0, 0)

    return answer

# def solution(numbers, target):
#     answer = 0
#     n = len(numbers)
#
#     def count(ans, cnt):
#         nonlocal answer
#         if cnt == n:
#             if ans == target:
#                 answer += 1
#             return
#         else:
#             ans += numbers[cnt]
#             count(ans, cnt + 1)
#             ans -= (numbers[cnt] * 2)
#             count(ans, cnt + 1)
#
#     count(0, 0)
#
#     return answer