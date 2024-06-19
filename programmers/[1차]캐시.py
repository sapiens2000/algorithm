from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    # 캐시 힛
    # 원래 원소 삭제 후 마지막에 추가

    # 캐시 없음
    # 1. 추가 (사이즈 적으면 or 사이즈 0)
    # 2. 교체 (사이즈 꽉 찼으면)

    for city in cities:
        city = city.lower()
        if city in cache:
            # 원래 원소 제거 후 끝에 추가
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if cacheSize != 0:
                if len(cache) == 0 or len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.popleft()
                    cache.append(city)
            answer += 5

    return answer