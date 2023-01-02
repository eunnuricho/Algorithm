N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

_min = cities[0]
sum = 0
for i in range(N - 1):
    if _min > cities[i]:
        _min = cities[i]
    sum += (_min * roads[i])

print(sum)