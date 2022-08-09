word = input().upper()
arr = []
ans = ''
max = 0

# word = input().upper()
# word_list = list(set(word))

for i in word:
    if i not in arr:
        arr.append(i)

#max 갱신
for j in arr:
    if word.count(j) > max:
        max = word.count(j)
        ans = j
    elif word.count(j) == max:
        ans = '?'

#max값 카운트
# if word.count(j) > 1:
#     print('?')
# else:
#     print(word[arr.index(max(arr))])

print(ans)