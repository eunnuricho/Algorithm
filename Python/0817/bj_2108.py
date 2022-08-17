import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

# 평균
print(round(sum(arr) / N))
# 중앙값
print(arr[N // 2])

## 최빈값
cnt_arr = Counter(arr).most_common()        #[(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)]
if len(cnt_arr) > 1 and cnt_arr[0][1]==cnt_arr[1][1]: #최빈값 2개 이상
    print(cnt_arr[1][0])
else:
    print(cnt_arr[0][0])

# 범위
print(max(arr) - min(arr))