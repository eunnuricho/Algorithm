import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    num = int(input())

    if num:
        hq.heappush(heap, (abs(num), num))


    else:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)

    # print(heap)