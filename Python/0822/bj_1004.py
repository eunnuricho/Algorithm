T = int(input())

for _ in range(T):
    # 출발점 도착점
    x1, y1, x2, y2 = list(map(int, input().split()))
    # 행성계의 개수
    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, cr = map(int, input().split()) # 각 행성의 x좌표, y좌표, 반지름
        dis1 = (x1 - cx) ** 2 + (y1 - cy) ** 2 # 출발점과 행성의 거리
        dis2 = (x2 - cx) ** 2 + (y2 - cy) ** 2 # 도착점과 행성의 거리
        pow_cr = cr ** 2 # 거리에 루트 안 씌워서 반지름에 제곱을 해줌

        if pow_cr > dis1 and pow_cr > dis2: # 출발점, 도착점 모두 행성 안에 있으면 카운트 x
            pass
        elif pow_cr > dis1: # 출발점과의 거리가 행성의 반지름보다 작으면 나가야 함
            count += 1
        elif pow_cr > dis2: # 도착점과의 거리가 행성의 반지름보다 작으면 들어가야 함
            count += 1

    print(count)