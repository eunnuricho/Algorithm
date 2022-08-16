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
# for i in people:
#     rank = 1
#     for j in people:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank+=1
#     print(rank, end = " ")
