T = int(input())

for tc in range(T):
    result = input()
    cnt = 0
    ans = 0

    for i in range(len(result)):
        if result[i] == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0

    print(ans)