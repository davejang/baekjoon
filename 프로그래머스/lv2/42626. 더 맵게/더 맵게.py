import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    
    while heap:
        answer += 1
        
        if len(heap) >= 2:
            a1 = heapq.heappop(heap)
            a2 = heapq.heappop(heap) * 2
            heapq.heappush(heap,a1 + a2)
            if heap[0] >= K:
                break
        else:
            answer = -1
            break
    return answer