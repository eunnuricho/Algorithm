N = int(input())
M = N
cnt = 0

while True:
    A = N // 10
    B = N % 10
    hap = (A + B) % 10
    new_N = B * 10 + hap

    if new_N != M:
        cnt += 1
        N = new_N
    else:
        print(cnt + 1)
        break