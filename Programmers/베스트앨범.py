def solution(genres, plays):
    answer = []
    dict = {}
    total = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in total.keys():
            total[genre] += play
            dict[genre].append((play, i))
        else:
            total[genre] = play
            dict[genre] = [(play, i)]

    total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    # print(total)
    # print(dict)

    for genre in total:
        play = dict[genre[0]]
        play = sorted(play, key=lambda x: x[0], reverse=True)
        for j in range(len(play)):
            if j < 2:
                answer.append(play[j][1])

    return answer
