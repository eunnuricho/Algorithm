import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    st, ed = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (ed, st))

# print(heap)

tmp = 0
cnt = 0

while heap:
    ed, st = heapq.heappop(heap)

    if st >= tmp:
        cnt += 1
        tmp = ed

print(cnt)
