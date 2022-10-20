def solution(clothes):
    answer = 0
    spy = {}
    for cloth in clothes:
        if cloth[1] not in spy:
            spy[cloth[1]] = [cloth[0]]
        else:
            spy[cloth[1]].append(cloth[0])

    a = len(spy.keys())
    b = 0

    # 000 100 010 001 110 011 101 111
    for key in spy:
        b += len(spy[key])

    # print(spy)
    # print((a, b))

    if a > 1:
        answer += (2 ** b) - a - 1
    else:
        answer += b
    return answer


# def solution(clothes):
#     answer = 0
#     spy = {}
#     for cloth in clothes:
#         if cloth[1] not in spy:
#             spy[cloth[1]] = [cloth[0]]
#         else:
#             spy[cloth[1]].append(cloth[0])
#
#     a = len(spy.keys())
#     b = 1
#
#     for key in spy:
#         b *= (len(spy[key]) + 1)
#
#     # print(spy)
#     # print((a, b))
#
#     answer = (b - 1)
#     return answer