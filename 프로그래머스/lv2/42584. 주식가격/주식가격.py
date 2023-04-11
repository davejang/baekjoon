from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        # 첫 번째 가격 pop
        price = queue.popleft()
        count = 0
        
        # 가격이 낮은 경우 종료
        for i in queue:
            count += 1
            if price > i:
                break
        
        answer.append(count)
            
    return answer