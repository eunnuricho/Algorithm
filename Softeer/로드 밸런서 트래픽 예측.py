import sys

def cal(arr):
    degree = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, len(arr[i])):
            degree[arr[i][j]] += 1
    return degree

def tsort(arr):
    indegree = cal(arr)

    stack = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            stack.append(i)

    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        for j in range(1, len(arr[node])):
            child = arr[node][j]
            indegree[child] -= 1
            if indegree[child] == 0:
                stack.append(child)
    return order


N, K = map(int, sys.stdin.readline().split())
arr = [[0]]

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)

ordering = tsort(arr)

traffic = [0] * (N + 1)
traffic[1] = K

for i in range(N):
    node = ordering[i]
    request = traffic[node]
    if len(arr[node]) == 1:
        continue

    q = request // arr[node][0]
    r = request % arr[node][0]

    for j in range(1, len(arr[node])):
        child = arr[node][j]
        traffic[child] += q
    for k in range(1, r + 1):
        child = arr[node][k]
        traffic[child] += 1

print(*traffic[1:])