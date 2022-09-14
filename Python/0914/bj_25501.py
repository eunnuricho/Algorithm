def recursion(s, l, r, cnt):
    if l >= r:
        print(1, cnt, sep=' ', end='\n')
        return
    elif s[l] != s[r]:
        print(0, cnt, sep=' ', end='\n')
        return
    else:
        return recursion(s, l+1, r-1, cnt + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)


T = int(input())

for _ in range(T):
    s = input()
    isPalindrome(s)
