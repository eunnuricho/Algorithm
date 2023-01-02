def multi(a, n):
    if n == 1:
        return a % C
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * a) % C


A, B, C = map(int, input().split())

print(multi(A, B))


# A^m+n = A^m x A^n
# (AxB)%C = (A%C) *(B%C) % C