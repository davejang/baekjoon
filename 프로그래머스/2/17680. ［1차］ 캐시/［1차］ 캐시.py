from collections import deque

def solution(cacheSize, cities):
    answer = 0
    hashSet = {}
    q = deque()
    
    for city in cities:
        cityCaseUpper = city.upper()
        if cityCaseUpper in q:
            q.remove(cityCaseUpper)
            q.appendleft(cityCaseUpper)
            answer += 1
        else:
            q.appendleft(cityCaseUpper)
            if len(q) > cacheSize:
                q.pop()
            answer += 5
            
    return answer