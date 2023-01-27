import heapq


def solution(operations):
    heap = []

    for o in operations:
        order, num = o.split()
        if order == 'I':
            heapq.heappush(heap, int(num))
        elif heap and order == 'D' and num == '-1':
            heapq.heappop(heap)
        elif heap and order == 'D' and num == '1':
            target = max(heap)
            heap.remove(target)

    if heap:
        return [max(heap), heap[0]]
    else:
        return [0, 0]
