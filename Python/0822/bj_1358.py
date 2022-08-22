w, h, x, y, p = map(int, input().split())

cnt = 0
for _ in range(p):  # 선수 p명
    a, b = map(int, input().split())    # 각각의 좌표

    # 직사각형 안에 포함인지
    if x <= a <= x + w and y <= b <= y + h:
        cnt += 1

    # 왼쪽 반원 안에 포함인지(x, y + (h / 2))
    elif a < x:
        if (a - x) ** 2 + (b - (y + (h / 2))) ** 2 <= (h / 2) ** 2:     # 반원 중심과의 거리가 반지름보다 작으면 포함
            cnt += 1

    # 오른쪽 반원 안에 포함인지(x + w, y + (h / 2))
    elif x < a:
        if (a - (x + w)) ** 2 + (b - (y + (h / 2))) ** 2 <= (h / 2) ** 2:   # 반원 중심과의 거리가 반지름보다 작으면 포함
            cnt += 1

print(cnt)