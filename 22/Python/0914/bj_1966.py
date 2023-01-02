import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))

    printer = []

    while len(q) > 0:
        tmp_max = max(q)
        tmp_value = q.popleft()
        M -= 1                          # 타겟의 위치 변화(한 칸 앞)

        if tmp_value == tmp_max:
            printer.append(tmp_value)

            if M < 0:
                print(len(printer))     # 타겟 프린트 차례
                break

        else:
            q.append(tmp_value)

            if M < 0:
                M = len(q) - 1          # 타겟의 위치 변화(맨 앞에서 맨 뒤)