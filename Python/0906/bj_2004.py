def cnt5(n):
    ans = 0
    while n != 0:
        n //= 5
        ans += n
    return ans

def cnt2(n):
    ans = 0
    while n != 0:
        n //= 2
        ans += n
    return ans


n, m = map(int, input().split())
print(min(cnt2(n) - cnt2(n - m) - cnt2(m), cnt5(n) - cnt5(n - m) - cnt5(m)))
