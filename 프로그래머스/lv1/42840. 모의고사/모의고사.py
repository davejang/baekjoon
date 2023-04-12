def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_count = 0
    b_count = 0
    c_count = 0
    
    for i in range(len(answers)):
        a_index = i % len(a)
        b_index = i % len(b)
        c_index = i % len(c)
        
        if a[a_index] == answers[i]:
            a_count += 1
        if b[b_index] == answers[i]:
            b_count += 1
        if c[c_index] == answers[i]:
            c_count += 1
    
    max_correct = max(a_count,b_count,c_count)
    
    if a_count == max_correct:
        answer.append(1)
    if b_count == max_correct:
        answer.append(2)
    if c_count == max_correct:
        answer.append(3)
    
    return answer