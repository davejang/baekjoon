import math
from collections import deque

def solution(progresses, speeds):
    work_queue = deque([])
    deploy = []
    for i in range(len(progresses)):
        work_time = math.ceil((100 - progresses[i]) / speeds[i])
        
        # 가장 앞의 기능이 완료되었을 경우 배포
        if work_queue:
            if work_queue[0] < work_time:
                deploy.append(len(work_queue))
                work_queue = deque([])
            
        work_queue.append(work_time)

    if work_queue:
        deploy.append(len(work_queue))
        
    return deploy