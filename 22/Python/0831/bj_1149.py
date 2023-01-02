import sys
input = sys.stdin.readline

N = int(input())
RGB = list(list(map(int, input().split())) for _ in range(N))

for j in range(1, N):
    RGB[j][0] += min(RGB[j - 1][1], RGB[j - 1][2])      # 빨강일 때 최솟값 => 이전 집을 초록이나 파랑으로 칠했을 때 중에 적은 값
    RGB[j][1] += min(RGB[j - 1][0], RGB[j - 1][2])      # 초록일 때 => 이전 집 빨강, 파랑
    RGB[j][2] += min(RGB[j - 1][0], RGB[j - 1][1])      # 파랑일 때 => 이전 집 빨강, 초록

print(RGB)
print(min(RGB[-1]))