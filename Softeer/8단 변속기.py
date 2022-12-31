import sys

trans = list(map(int, sys.stdin.readline().split()))
comp = sorted(trans)

if trans == comp:
    print('ascending')
elif trans == comp[::-1]:
    print('descending')
else:
    print('mixed')