import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)

    while True:
        if len(scoville) < 2:
            answer = -1
            break
        else:
            if scoville[0] < K:
                answer += 1
                tmp1 = heapq.heappop(scoville)
                tmp2 = heapq.heappop(scoville)
                new = tmp1 + (tmp2 * 2)
                heapq.heappush(scoville, new)
            else:
                break

    return answer


# import heapq
#
#
# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)
#     # print(scoville)
#
#     while True:
#         if len(scoville) < 2 and scoville[0] < K:
#             answer = -1
#             break
#         if scoville[0] < K:
#             answer += 1
#             tmp1 = heapq.heappop(scoville)
#             tmp2 = heapq.heappop(scoville)
#             new = tmp1 + (tmp2 * 2)
#             heapq.heappush(scoville, new)
#         else:
#             break
#
#     return answer