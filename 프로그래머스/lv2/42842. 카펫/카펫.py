def solution(brown, yellow):
    answer = []
    case = []
    size = brown + yellow
    
    for i in range(3,size//2):
        if size % i == 0:
            case.append((i,int(size/i)))
    
    print(case)
    
    for i, j in case:
        if (i * 2) + (j * 2) - 4 == brown:
            answer.append(j)
            answer.append(i)
            break
        
    return answer