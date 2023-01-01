import sys

N, M = map(int, sys.stdin.readline().split())

rooms = {}

for i in range(N):
    room = sys.stdin.readline().strip()
    rooms[room] = [0] * 18 + [1]

for j in range(M):
    target, start, end = sys.stdin.readline().split()
    start = int(start)
    end = int(end)

    for k in range(start, end):
        rooms[target][k] = 1

rooms = sorted(rooms.items())

for l in range(N):
    curr = 1
    tmp = []

    for m in range(9, 19):
        if curr == 1 and rooms[l][1][m] == 0:
            st = m
            curr = 0
        elif curr == 0 and rooms[l][1][m] == 1:
            ed = m
            curr = 1
            tmp.append([st, ed])

    print(f'Room {rooms[l][0]}:')

    if len(tmp) == 0:
        print('Not available')

    else:
        print(len(tmp), 'available:')

        for n in range(len(tmp)):
            print(f'{tmp[n][0]:02d}-{tmp[n][1]}')

    if l != N - 1:
        print('-----')