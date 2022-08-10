# 1/1 - 1/2, 2/1 - 3/1, 2/2, 1/3, .........

X = int(input())

line = 0  # 사선 라인
total = 0  # 누적된 분수의 개수

while X > total:
    line += 1
    total += line

gap = total - X #마지막 개수에서 얼마나 떨어져 있는지

if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
    top = line - gap  # 분자
    under = gap + 1  # 분모

else:  # 사선 라인이 홀수번째 일 때
    top = gap + 1  # 분자
    under = line - gap  # 분모

print(f'{top}/{under}')