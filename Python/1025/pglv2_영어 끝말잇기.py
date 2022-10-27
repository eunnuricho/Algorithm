def solution(n, words):
    answer = []
    used = []
    people = {}

    used.append(words[0])
    people[1] = 1

    for i in range(2, n + 1):
        people[i] = 0

    for j in range(1, len(words)):
        people[(j % n) + 1] += 1
        if words[j] in used or words[j][0] != used[-1][-1]:
            answer.append((j % n) + 1)
            answer.append(people[(j % n) + 1])
            break
        else:
            used.append(words[j])

    if not answer:
        answer.append(0)
        answer.append(0)

    return answer

# def solution(n, words):
#     cnt = 0
#     end_word = words[0][0]
#     check = set()
#     for word in words:
#         if word in check or end_word != word[0]:
#             return [(cnt%n)+1, (cnt//n)+1]
#         end_word = word[-1]
#         check.add(word)
#         cnt += 1
#     return [0, 0]