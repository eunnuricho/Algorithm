import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    num = int(input())

    if num:
        hq.heappush(heap, num)      # 최소 힙

    else:
        if heap:
            print(hq.heappop(heap))
        else:
            print(0)

    # print(heap)