def solution(array):
    answer = 0
    dict = {}

    # 세트로 만들지 않으면 계속 value값이 갱신됨......
    # for i in range(len(array)):
    #     dict[array[i]] = array.count(array[i])
    #
    # arr = []
    #
    # for key in dict.keys():
    #     if dict[key] == max(dict.values()):
    #         arr.append(dict[key])

    nums = set(array)

    for num in nums:
        dict[num] = array.count(num)

    arr = []

    for num in nums:
        if dict[num] == max(dict.values()):
            arr.append(num)

    # print(arr)
    if len(arr) >= 2:
        answer = -1
    else:
        answer = arr[0]

    return answer