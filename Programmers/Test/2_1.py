def solution(cacheSize, cities):
    cache = []
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()

        if city in cache:
            cache.remove(city)
            cache.insert(len(cities) - 1, city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)

            cache.append(city)
            answer += 5

    return answer
