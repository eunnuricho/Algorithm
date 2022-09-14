import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    num = int(input())

    if num:
        if num < 0:
            hq.heappush(heap, (num * -1, num))      # 절대값, 그냥 값
        else:
            hq.heappush(heap, (num, num))


    else:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)

    # print(heap)