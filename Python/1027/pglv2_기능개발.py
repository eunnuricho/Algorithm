from collections import deque

def solution(progresses, speeds):
    answer = []

    q1 = deque(progresses)
    q2 = deque(speeds)
    days = 0
    arr = []

    for i in range(len(progresses)):
        target = q1.popleft()
        s = q2.popleft()
        target += (s * days)
        while target < 100:
            target += s
            days += 1
        arr.append(days)

    tmp = set()
    for a in arr:
        if a not in tmp:
            answer.append(arr.count(a))
        tmp.add(a)

    return answer