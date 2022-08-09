T = int(input())

for tc in range(T):
    times, letters = input().split()
    ans = ''
    for i in range(len(letters)):
        ans += letters[i] * int(times)

    # for l in letters:
    #     print(l * int(times), end='')
    # print()

    print(ans)