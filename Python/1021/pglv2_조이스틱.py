def solution(name):
    answer = 0
    arr = list(name)
    init = list('A' * len(name))
    n = len(arr)

    change = 0
    move = 0
    curr = 0
    visited = [0 for _ in range(len(name))]

    while True:
        if ''.join(init) == ''.join(arr):
            break
        else:
            if not visited[curr] and init[curr] != arr[curr]:
                change += min(abs(ord(init[curr]) - ord(name[curr])),
                              abs(ord(init[curr]) - ord('A') + 1 + ord('Z') - ord(name[curr])))
                visited[curr] = 1
            for i in range(n - 1):
                tmp = []
                if not visited[curr + i] and arr[curr + i] != 'A':
                    tmp.append([i, curr + i])
                if not visited[curr - i] and arr[curr - i] != 'A':
                    tmp.append([i, curr - i])
            tmp.sort()
            move += tmp[0][0]
            curr = tmp[0][1]

    answer += (change + move)
    return answer