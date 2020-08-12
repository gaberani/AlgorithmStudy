def solution(cacheSize, cities):
    answer = 0
    cache = []
    for word in cities:
        word = word.lower()
        if len(cache) < cacheSize:
            if word not in cache:
                answer += 5
                cache.append(word)
            else:
                answer += 1
                cache.pop(cache.index(word))
                cache.append(word)
        elif len(cache) == cacheSize:
            if cacheSize == 0:
                answer += 5
            else:
                if word not in cache:
                    answer += 5
                    cache.pop(0)        # 맨 앞에 뺌
                    cache.append(word)
                else:
                    answer += 1
                    cache.pop(cache.index(word))
                    cache.append(word)
    return answer

print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(2, ['Jeju', 'Pangyo', 'NewYork', 'newyork']))