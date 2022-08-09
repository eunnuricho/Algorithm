word = input()
arr2 = ['A', 'B', 'C']
arr3 = ['D', 'E', 'F']
arr4 = ['G', 'H', 'I']
arr5 = ['J', 'K', 'L']
arr6 = ['M', 'N', 'O']
arr7 = ['P', 'Q', 'R', 'S']
arr8 = ['T', 'U', 'V']
arr9 = ['W', 'X', 'Y', 'Z']
ans = 0

for i in range(len(word)):
    if word[i] in arr2:
        ans += 3
    elif word[i] in arr3:
        ans += 4
    elif word[i] in arr4:
        ans += 5
    elif word[i] in arr5:
        ans += 6
    elif word[i] in arr6:
        ans += 7
    elif word[i] in arr7:
        ans += 8
    elif word[i] in arr8:
        ans += 9
    elif word[i] in arr9:
        ans += 10

print(ans)

# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)