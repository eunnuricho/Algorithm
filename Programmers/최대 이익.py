def solution(n, v):
    max_profit = v[0] - v[1]
    max_price = max(v[0], v[1])

    for i in range(2, n):
        max_profit = max(max_profit, max_price - v[i])
        max_price = max(max_price, v[i])

    return max_profit