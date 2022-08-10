word = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

arr = [-1] * 26

for a in alpha:
    if a in word:
        arr[alpha.index(a)] = word.index(a)

print(*arr)

#find + 아스키코드
# alpha = list(range(97, 123))
#
# for a in alpha:
#     print(word.find(chr(a)), end=' ')