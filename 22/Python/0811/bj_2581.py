M = int(input())
N = int(input())
arr = []

for num in range(M, N + 1):
    _flag = True
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            _flag = False
            break

    if _flag == True:
        arr.append(num)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr), min(arr), sep='\n')

#1. 배열을 안써본다
#2. flag를 안써본다
#3. 둘 다 안 써본다