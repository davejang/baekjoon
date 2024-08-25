import heapq

def solution(food_times, k):
    q = []
    # k가 총 시간보다 적을 경우 섭취해야 할 음식 없음
    if sum(food_times) <= k:
        return -1
    
    # 잔여 시간 오름차순
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
        
    length = len(food_times)
    time = 0
    prev_time = 0
    
    # 현재 시간 + (대상 시간 * 남은 길이) <= k일 경우 수행
    while time + ((q[0][0] - prev_time) * length) <= k:
        cur_time, index = heapq.heappop(q)
        time += (cur_time - prev_time) * length
        length -= 1
        prev_time = cur_time
        
    q.sort(key=lambda x:x[1])
    return q[(k-time) % length][1]