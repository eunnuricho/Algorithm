import sys
input = sys.stdin.readline

N = int(input())
arr = list([0] * 2 for _ in range(N))

for i in range(N):
    _start, _finish = map(int, input().split())
    arr[i][0], arr[i][1] = _start, _finish

arr.sort(key=lambda x: (x[1], x[0]))        # 빨리 끝나는 순서 -> 빨리 시작하는 순서로 정렬

cnt = 1
_end = arr[0][1]

for j in range(1, N):
    if arr[j][0] >= _end:       # 종료 이후 시작하는 회의이면
        cnt += 1
        _end = arr[j][1]

print(cnt)