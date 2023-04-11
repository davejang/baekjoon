from collections import deque

def solution(priorities, location):
    answer = 0
    printer = deque(priorities)
    max_val = max(printer)
    
    while True:
        # 문서 뽑아오기
        doc = printer.popleft()
        
        # 중요도가 가장 높을 경우 프린트
        if doc == max_val:
            answer += 1
            if location == 0:
                break
            max_val = max(printer)
            
        # 중요도가 높지 않을 경우 뒤로 이동
        else:
            printer.append(doc)
            
        # location이 처음일 경우 
        if location == 0:
            location = len(printer) - 1
        else:
            location -= 1
            
    return answer