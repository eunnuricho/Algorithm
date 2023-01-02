N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if cards[i] + cards[j] + cards[k] > M:
                continue
            else:
                ans = max(ans, cards[i] + cards[j] + cards[k])

print(ans)

# combination 라이브러리

# from itertools import combinations
#
# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
#
# ans = 0
#
# for card in combinations(cards, 3):
#     tmp = sum(card)
#     if ans < tmp <= M:
#         ans = tmp
#
# print(ans)