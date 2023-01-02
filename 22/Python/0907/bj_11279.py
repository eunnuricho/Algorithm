import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    num = int(input())

    if num:
        hq.heappush(heap, -num)      # 제일 큰 값이 0번째 튜플의 두 번째에 위치

    else:
        if heap:
            print(hq.heappop(heap) * -1)
        else:
            print(0)

    # print(heap)