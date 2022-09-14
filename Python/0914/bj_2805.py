N, M = map(int, input().split())
trees = list(map(int, input().split()))
st, ed = 1, sum(trees)


while st <= ed:
    H = (st + ed) // 2
    ans = 0

    for tree in trees:
        if H < tree:
            ans += (tree - H)      # 잘라진 나무 길이

    if ans >= M:
        st = H + 1

    else:
        ed = H - 1

# print(st)
print(ed)