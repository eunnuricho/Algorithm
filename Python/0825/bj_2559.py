N, K = map(int, input().split())
record = list(map(int, input().split()))

ans = []
ans.append(sum(record[:K]))

for i in range(N - K):
    ans.append(ans[i] - record[i] + record[i + K])

print(max(ans))