arr = list(list(map(int, input().split())) for _ in range(9))

ans = -1
r, c = 0, 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > ans:
            ans = arr[i][j]
            r, c = i + 1, j + 1

print(ans)
print('{} {}'.format(r, c))