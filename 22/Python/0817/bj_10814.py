import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    age, name =map(str, sys.stdin.readline().split())
    age = int(age)
    arr.append((age, name))

arr.sort(key = lambda x : x[0])

for member in arr:
    print(member[0], member[1])