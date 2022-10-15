import heapq

def solution(n, works):
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap,-work)
    
    while n > 0:
        work = heapq.heappop(heap) + 1
        n -= 1
        if work > 0:
            work = 0
        heapq.heappush(heap,work)
        
    for i in heap:
        answer += i*i
        
    return answer