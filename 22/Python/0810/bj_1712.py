A, B, C = map(int, input().split())

if B >= C:
    print(-1)

# 노트북 n대 판매했을 때
# cost = A + (B * n) -> 비용
# sales = C * n -> 수입
#
# 비용과 수입이 같다고 가정했을 때의 n
# cost = sales
#
# A + (B * n) = C * n
# A = (C * n) - (B * n)
# A = (C - B) * n
# 얘가 0보다 커야하므로 + 1
# (A // (C - B)) = n

else:
    print((A // (C - B)) + 1)