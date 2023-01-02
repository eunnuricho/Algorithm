def solution(phone_book):
    answer = True
    dict = {}
    for phone_number in phone_book:
        dict[phone_number] = 1

    for phone_number in phone_book:
        tmp = ''
        for number in phone_number:
            tmp += number
            if tmp in dict and tmp != phone_number:
                answer = False
    return answer