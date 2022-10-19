def solution(s):
    answer = ''

    arr = s.split()
    lst = []
    for i in range(len(arr)):
        word = ''
        for j in range(len(arr[i])):
            tmp = arr[i][j]
            if j == 0:
                if ord(arr[i][j]) >= 65:
                    if arr[i][j].islower():
                        tmp = arr[i][j].upper()
            else:
                if ord(arr[i][j]) >= 65:
                    if arr[i][j].isupper():
                        tmp = arr[i][j].lower()
            word += tmp
        lst.append(word)

    answer = ' '.join(lst)
    #외않되 외 외 외 외
    return answer


# def solution(s):
#     answer = ''
#
#     arr = s.split(' ')
#     print(arr)
#
#     lst = []
#     for i in range(len(arr)):
#         word = ''
#         for j in range(len(arr[i])):
#             tmp = arr[i][j]
#             if j == 0:
#                 tmp = arr[i][j].upper()
#             else:
#                 tmp = arr[i][j].lower()
#             word += tmp
#         lst.append(word)
#
#     answer = ' '.join(lst)
#
#     return answer