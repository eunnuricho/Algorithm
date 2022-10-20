def solution(numbers):
    answer = ''
    tmp = str(max(numbers))
    len_tmp = len(tmp) - 1

    new = []
    for num in numbers:
        if num < (10 ** len_tmp):
            new.append([num * (10 ** len_tmp), num])
        else:
            new.append([num])
    new.sort()
    new = new[::-1]

    for n in new:
        answer += str(n[-1])

    return answer


# def solution(numbers):
#     answer = ''
#
#     new = []
#     for num in numbers:
#         if num < (10 ** 4):
#             new.append((int((str(num) * 4)[:4]) * -1, num))
#         else:
#             new.append((num * -1, num))
#     new.sort()
#     # print(new)
#     for n in new:
#         answer += str(n[1])
#
#     # 15, 151 -> [151, 151]
#     # 15, 151 -> [1515, 1511]
#     return str(int(answer))