import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = dict()
    for i in range(n):
        name, category = input().split()
        if clothes.get(category) == None:
            clothes[category] = []
        clothes[category].append(name)

    cnt = 1
    for key in clothes.keys():
        cnt *= len(clothes[key]) + 1

    print(cnt - 1)