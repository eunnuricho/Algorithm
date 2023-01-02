T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())
    total = 0 #배정될 라인까지 총 방의 개수
    cnt = 0 #배정될 방의 라인(걸어야하는 거리)

    while total < N:
        total += H
        cnt += 1

    gap = total - N

    #라인 끝 방 넘버 -> H + cnt 호

    if cnt < 10:
        ans = str(H - gap) + str(0) + str(cnt)
    else:
        ans = str(H - gap) + str(cnt)

    print(ans)