N = int(input())
_flag = True
cnt = 0

for _ in range(N):
    word = input()
    repeat = []


    for i in range(len(word)):
        if word[i] not in repeat:
            repeat.append(word[i])
        else:
            if repeat[-1] != word[i]:
                _flag = False
                break

    if _flag == True:
        cnt += 1
    else:
        _flag = True

print(cnt)


# N = int(input())
# cnt = N
#
# for i in range(N):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             cnt -= 1
#             break
#
# print(cnt)