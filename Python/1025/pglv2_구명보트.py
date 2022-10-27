def solution(people, limit):
    n = len(people)
    answer = n

    people.sort(reverse=True)
    a = 0
    b = -1
    saved = 0
    while True:
        target = people[a]
        saved += 1
        a += 1
        if saved == n:
            break
        if target + people[b] <= limit:
            saved += 1
            b -= 1
            answer -= 1
            if saved == n:
                break

    return answer