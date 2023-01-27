def solution(priorities, location):
    answer = 0

    while True:
        printing = max(priorities)
        for i in range(len(priorities)):
            if printing == priorities[i]:
                answer += 1
                priorities[i] = 0
                printing = max(priorities)

                if i == location:
                    return answer
