import heapq

def solution(targets):
    q = []
    answer = 1
    
    targets.sort(key=lambda x:x[0])
    
    for s, e in targets:
        if not q:
            heapq.heappush(q,e)
        else:
            if s < q[0]:
                heapq.heappush(q,e)
            else:
                while q:
                    heapq.heappop(q)
                heapq.heappush(q,e)
                answer += 1
    
    return answer