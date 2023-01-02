import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = list(int(input()) for _ in range(K))
st, ed = 1, max(lans)


while st <= ed:
    mid = (st + ed) // 2
    ans = 0

    for lan in lans:
        ans += (lan // mid)

    if ans >= N:
        st = mid + 1

    else:
        ed = mid - 1

print(ed)