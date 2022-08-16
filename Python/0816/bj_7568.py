N = int(input())
arr = []
ans = []

for _ in range(N):
    stat = list(map(int, input().split()))
    arr.append(stat)

for i in range(N):
    cnt = 0
    pointer = 0

    while pointer < N:
        if pointer != i:
            if arr[i][0] < arr[pointer][0] and arr[i][1] < arr[pointer][1]:
                cnt += 1
        pointer += 1
    else:
        ans.append(cnt + 1)

print(*ans)

# N = int(input())
# people = []
#
# for _ in range(N):
#     x, y = map(int, input().split())
#     people.append((x,y))
#
# for w1, h1 in people:
#     rank = 1
#     fo:r w2, h2 in people
#         if w1 < w2 and h1 < h2:
#             rank+=1
#     print(rank, end = " ")
