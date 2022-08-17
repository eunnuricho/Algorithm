N, k = map(int, input().split())
scores = list(map(int, input().split()))

#버블로 내림차순 왼쪽부터 k개까지 정렬
for i in range(N - 1):
    for j in range(N - 1, i, -1):
        if scores[j] > scores[j - 1]:
            scores[j], scores[j - 1] = scores[j - 1], scores[j]
    if i == k - 1:
        break

print(scores[k - 1])