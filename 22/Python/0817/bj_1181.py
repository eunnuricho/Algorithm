import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(sys.stdin.readline().strip())

words = list(set(arr))

li = []
for word in words:
    li.append((len(word), word))

ans = sorted(li)

for l, w in ans:
    print(w)

# import sys
# input = sys.stdin.readline
#
# words = []
# for i in range(int(input())):
#   words.append(input().rstrip())
#
# words = sorted(list(set(words)), key = lambda x : (len(x),x))
#
# print('\n'.join(words))
