N = int(input())
scores = list(map(int, input().split()))
_max = max(scores)

new = []
for i in range(N):
    new.append((scores[i] / _max) * 100)

print(sum(new) / N)

# for i in range(N):
#     scores[i] = ((scores[i]) / _max) * 100
#
# print(sum((scores)) / N)