import sys

input = sys.stdin.readline

N = int(sys.stdin.readline())
cards = list(map(int, input().split()))
M = int(sys.stdin.readline())
nums = list(map(int, input().split()))

_dict = {}

# for i in range(N):
#     _dict[cards[i]] = cards.count(cards[i])
#
# for num in nums:
#     print(_dict[num], end=' ') if num in _dict else print(0, end=' ')

for card in cards:
    if card in _dict:
        _dict[card] += 1
    else:
        _dict[card] = 1

for num in nums:
    ans = _dict.get(num)
    if ans:
        print(ans, end=' ')
    else:
        print(0, end=' ')