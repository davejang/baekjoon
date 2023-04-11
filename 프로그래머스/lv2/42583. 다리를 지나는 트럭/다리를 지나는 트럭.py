from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_queue = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    current_weight = 0
    
    
    while bridge:
        answer += 1
        w = bridge.popleft()
        current_weight -= w
        
        if truck_queue:
            # 다리 위에 트럭이 올라갈 수 있을 경우 트럭 추가
            if current_weight + truck_queue[0] <= weight:
                truck = truck_queue.popleft()
                current_weight += truck
                bridge.append(truck)
            # 트럭이 남아있을 경우 다리길이 유지
            else:
                bridge.append(0)

    return answer