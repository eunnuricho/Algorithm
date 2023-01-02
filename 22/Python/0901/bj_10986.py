N, M = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = [0 for _ in range(M)]

s = 0
num = 0
for i in range(N):
    s += arr_n[i]
    res = s % M

    if res == 0:
        num += 1        # 나머지가 0인 구간 합의 개수

    arr_m[res] += 1     # 나머지가 각각 0, 1, 2인 구간 합의 개수

for i in range(M):
    if arr_m == 0:
        continue

    num += arr_m[i] * (arr_m[i] - 1) // 2       # 나머지가 같은 구간 합 중에서 2개를 고르는 조합의 개수

print(num)