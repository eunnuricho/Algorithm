x, y, w, h = map(int, input().split())

#(10, 3) (9, 3) (8, 3) (7, 3) ...... (0, 3)
#(10, 2) (10, 1) (10, 0)

print(min(x, y, w-x, h-y))