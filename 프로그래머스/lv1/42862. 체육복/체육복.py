def solution(n, lost, reserve):
    answer = 0
    dict = {}
    for key in range(1,n+1):
        dict[key] = 1
    for key in reserve:
        dict[key] += 1
    for key in lost:
        dict[key] -= 1

    dict[0] = 1
    dict[n+1] = 1
    
    for i in range(1,n+1):
        
        # 여벌 옷이 있을 때
        if dict[i] > 1:
            # 앞사람 옷이 없으면 앞사람에게 빌려줌
            if dict[i-1] == 0:
                dict[i] = 1
                dict[i-1] = 1
            # 앞사람이 옷이 있고 뒷사람 옷이 없으면 뒷사람에게 빌려줌
            elif dict[i-1] >= 1 and dict[i+1] == 0:
                dict[i] = 1
                dict[i+1] = 1
            
            
    for i in range(1,n+1):
        if dict[i] > 0:
            answer += 1
            
    return answer