A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')


# A, B = map(int, input().split())
# print('>') if A > B else print('<') if A < B else print('==')