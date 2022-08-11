def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

T = int(input())

for tc in range(T):
    n = int(input())
    arr = []
    ans = []

    for i in range(2, n):
        if isPrime(i):
            arr.append(i)

    for k in arr:
        if (n - k) in arr:
            # 파티션, 두 소수의 차이
            ans.append([k, n - k, abs(k - (n - k))])

    if len(ans) > 2:
        # 두 번째 인덱스(차이)로 정렬
        ans.sort(key=lambda x: x[2])
        print(*ans[0][:2], sep=' ')
    else:
        print(*ans[0][:2], sep=' ')


    # a, b = n // 2, n // 2
    # while a > 0:
    #     if isPrime(a) and isPrime(b):
    #         print(a, b)
    #     else:
    #         a -= 1
    #         b += 1
