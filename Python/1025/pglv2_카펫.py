# def solution(brown, yellow):
#     answer = []
#     width = 0
#     length = 0
#
#     for i in range(1, 5000):
#         for j in range(i, 5000):
#             edge = ((i + j) * 2) - 4
#             if edge + yellow == i * j:
#                 width = j
#                 length = i
#                 break
#
#     answer.append(width)
#     answer.append(length)
#     return answer

def solution(brown, yellow):
    width = 0
    length = 0

    for i in range(3, 5000):
        for j in range(i, 5000):
            if brown + yellow == i * j and yellow == (i - 2) * (j - 2):
                width = j
                length = i
                return([width, length])