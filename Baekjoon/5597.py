dict = {}
for i in range(1, 31):
    dict[i] = 0

for j in range(28):
    dict[int(input())] = 1

for k in range(1, 31):
    if not dict[k]:
        print(k)