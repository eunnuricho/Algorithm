import sys

M, N, K = map(int, sys.stdin.readline().split())

if M > N:
    print('normal')
else:
    secret = list(map(int, sys.stdin.readline().split()))
    control = list(map(int, sys.stdin.readline().split()))
    ans = ''

    for i in range(len(control) - len(secret) + 1):
        if control[i:len(secret) + i] == secret:
            ans = 'secret'
    if not ans:
        ans = 'normal'

    print(ans)