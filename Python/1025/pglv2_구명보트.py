# def solution(people, limit):
#     n = len(people)
#     answer = n
#
#     people.sort(reverse=True)
#
#     saved = 0
#     while True:
#         target = people.pop(0)
#         saved += 1
#         if saved == n:
#             break
#         if target + people[-1] <= limit:
#             saved += 1
#             answer -= 1
#             if saved == n:
#                 break
#
#     return answer